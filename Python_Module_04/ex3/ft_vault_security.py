def ft_vault_security() -> None:
    try:
        print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
        print("Initiating secure vault access...")
        secure_data = "[CLASSIFIED] New security protocols archived"
        with open("classified_data.txt") as f:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            data = f.read()
            print(data)
            print()
        with open("security_protocols.txt", "w") as f:
            print("SECURE PRESERVATION:")
            f.write(secure_data)
            print(secure_data)
            print("Vault automatically sealed upon completion")
            print()
    except (IsADirectoryError, FileNotFoundError, PermissionError) as e:
        print(f"\nError {e.__class__.__name__}: {e}")


if __name__ == "__main__":
    ft_vault_security()
