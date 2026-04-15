def ft_ancient_text() -> None:
    file: str = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    fd = None
    try:
        print(f"Accessing Storage Vault: {file}")
        fd = open(file)
        print("Connection established...")
        print("\nRECOVERED DATA:")
        data = fd.read()
        print(data)
        print("\nData recovery complete. Storage unit disconnected.")
    except (IsADirectoryError, FileNotFoundError, PermissionError):
        print("ERROR: Storage vault not found. Run data generator first.")
    finally:
        if fd:
            fd.close()


if __name__ == "__main__":
    ft_ancient_text()
