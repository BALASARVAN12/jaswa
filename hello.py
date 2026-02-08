import os
import ipaddress
import sys


def validate_private(value: str):
    try:
        net = ipaddress.IPv4Network(value, strict=False)

        if net.is_private:
            print(f"VALID PRIVATE: {net}")
            return True
        else:
            print("ERROR: Not a private IP/subnet")
            return False

    except ValueError:
        print("ERROR: Invalid IP format")
        return False


if __name__ == "__main__":
    # Read value from GitHub workflow input
    user_value = os.getenv("IP_INPUT")

    if not user_value:
        print("ERROR: No input provided from workflow")
        sys.exit(1)

    print(f"Received from workflow: {user_value}")

    if not validate_private(user_value):
        sys.exit(1)   # Fail the workflow
