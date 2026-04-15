def ft_archive_creation() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    data = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]
    file = "new_discovery.txt"
    fd = None
    try:
        print(f"Initializing new storage unit: {file}")
        fd = open(file, "w")
        print("Storage unit created successfully...")
        print("\nInscribing preservation data...")
        for i in data:
            fd.write(i + "\n")
            print(i)
    except (IsADirectoryError, FileNotFoundError, PermissionError):
        print("ERROR: Storage vault not found")
    finally:
        if fd:
            fd.close()
            print("\nData inscription complete. Storage unit sealed.")
            print(f"Archive '{file}' ready for long-term preservation.")


if __name__ == "__main__":
    ft_archive_creation()
