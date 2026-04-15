import sys
import os
try:
    from dotenv import load_dotenv
except Exception as e:
    print(e.__class__.__name__, e)
    sys.exit(1)


def get_config() -> dict[str, str]:
    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL", ""),
        "API_KEY": os.getenv("API_KEY", ""),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "DEBUG"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT", ""),
    }


def display_config(config: dict[str, str]) -> None:
    print("Configuration loaded:")
    print("Mode:", config['MATRIX_MODE'])
    if config['DATABASE_URL']:
        print("Database: Connected to local instance")
    else:
        print("Database: [MISSING] DATABASE_URL not set")
    if config['API_KEY']:
        print("API Access: Authenticated")
    else:
        print("API Access: [MISSING] API_KEY not set")
    print("Log Level:", config['LOG_LEVEL'])
    if config['ZION_ENDPOINT']:
        print("Zion Network: Online")
    else:
        print("Zion Network: [MISSING] ZION_ENDPOINT not set")
    print()


def security_check(override: bool) -> None:
    print("Environment security check:")
    secrets = ["MATRIX_MODE", "DATABASE_URL",
               "API_KEY", "LOG_LEVEL",
               "ZION_ENDPOINT"]
    all_vars = {**globals(), **locals()}
    hardcoded = False
    for i in all_vars:
        if i.upper() in secrets:
            hardcoded = True
    if hardcoded:
        print("[KO] Hardcoded secrets detected!")
    else:
        print("[OK] No hardcoded secrets detected")

    config = True
    for i in secrets:
        if not os.getenv(i):
            config = False
    if config:
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file not properly configured")
    if override:
        print("[OK] Running in production mode")
    else:
        print("[OK] Production overrides available")


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...\n")
    override = True
    load_dotenv(override=override)
    config = get_config()
    display_config(config)
    security_check(override=override)
    print("\nThe Oracle sees all configurations.")
