import sys


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    try:
        archivist_id = input("Input Stream active. Enter archivist ID: ")
        report = input("Input Stream active. Enter status report: ")
    except (EOFError, KeyboardInterrupt):
        print("\nError: program has been interrupt")
        return
    print()
    print(f"[STANDARD] Archive status from {archivist_id}: {report}")
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete")
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    ft_stream_management()
