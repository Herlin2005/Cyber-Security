import hashlib
import getpass
import time
import sys

try:
    import requests
except ImportError:
    print("Error: Install the 'requests' library first with: pip install requests")
    sys.exit(1)

def check_password_breach(password):
    """Check if password exists in HIBP database"""
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]

    try:
        time.sleep(1.5)  # Respect API rate limits
        response = requests.get(
            f"https://api.pwnedpasswords.com/range/{prefix}",
            headers={"User-Agent": "Python-Password-Checker"},
            timeout=5
        )
        response.raise_for_status()

        for line in response.text.splitlines():
            if line.split(':')[0] == suffix:
                return True, int(line.split(':')[1])
        return False, 0

    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}", file=sys.stderr)
        return None, 0

def main():
    print("=== Password Breach Checker ===")
    password = getpass.getpass("Enter password (input hidden): ").strip()

    if not password:
        print("Error: No password entered.", file=sys.stderr)
        return

    is_breached, count = check_password_breach(password)

    if is_breached is None:
        print("Failed to check due to network error.", file=sys.stderr)
    elif is_breached:
        print(f"\033[91mALERT: Password found in {count:,} breaches!\033[0m")
    else:
        print("\033[92mPassword not found in breaches.\033[0m")

if __name__ == "__main__":
    main()