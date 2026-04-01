def ft_crisis_response(file: str) -> None:
    try:
        with open(file) as f:
            data = f.read()
            print(f"ROUTINE ACCESS: Attempting access to '{file}'...")
            print(f"SUCCESS: Archive recovered - ``{data}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except IsADirectoryError:
        print(f"CRISIS ALERT: Attempting access to '{file}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")


if __name__ == "__main__":
    try:
        print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
        ft_crisis_response("lost_archive.txt")
        print()
        ft_crisis_response("classified_vault.txt")
        print()
        ft_crisis_response("standard_archive.txt")
        print("\nAll crisis scenarios handled successfully. Archives secure.")
    except Exception as e:
        print(f"Error {e.__class__.__name__}: {e}")
