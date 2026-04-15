from typing import Generator


def events_generator(n: int) -> Generator[dict[str, int | str], None, None]:
    players: list[str] = ["alice", "bob",
                          "charlie", "sisi", "marouane", "jack"]
    events: list[str] = ["killed monster", "found treasure", "leveled up",
                         "killed boss", "found silver", "found ghost",
                         "killed ghost", "helper"]
    for i in range(n):
        name_idx = i % len(players)
        event_idx = i % len(events)
        level = ((i + len(players)) * ((name_idx * 7) * event_idx) % 24) + 1
        yield {
            "event_id": i + 1,
            "name": players[name_idx],
            "level": level,
            "event": events[event_idx]
        }


def fibonacci_generator(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(n: int) -> Generator[int, None, None]:
    found = 0
    num = 2

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    while found < n:
        if is_prime(num):
            yield num
            found += 1
        num += 1


def main() -> None:
    first = True
    events = 1000
    prime_nbr = 5
    fibo_nbr = 10
    nbr_treasure = 0
    nbr_leveled_up = 0
    nbr_high_level = 0
    print("=== Game Data Stream Processor ===\n")
    print(f"Processing {events} game events...")
    for player in events_generator(events):
        if player['event_id'] < 4:
            print(
                f"Event {player['event_id']}: Player {player['name']} "
                f"(level {player['level']}) {player['event']}"
            )
        elif player['event_id'] == 4:
            print("...")
        if player["level"] >= 10:
            nbr_high_level += 1
        if player["event"] == "found treasure":
            nbr_treasure += 1
        elif player["event"] == "leveled up":
            nbr_leveled_up += 1
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {events}")
    print(f"High-level players (10+): {nbr_high_level}")
    print(f"Treasure events: {nbr_treasure}")
    print(f"Level-up events: {nbr_leveled_up}")
    print("\nMemory usage: Constant (streaming)")
    print("\n=== Generator Demonstration ===")
    print(f"Fibonacci sequence (first {fibo_nbr}): ", end="")
    for i in fibonacci_generator(fibo_nbr):
        if first:
            print(i, end="")
            first = False
        else:
            print(f", {i}", end="")
    print()
    print(f"Prime numbers (first {prime_nbr}): ", end="")
    first = True
    for i in prime_generator(prime_nbr):
        if first:
            print(i, end="")
            first = False
        else:
            print(f", {i}", end="")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nError: KeyboardInterrupt")
