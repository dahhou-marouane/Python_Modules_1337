import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    scores: list[int] = []
    argc = len(sys.argv)
    if argc == 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
            )
        return
    else:
        i = 1
        for i in sys.argv[1:]:
            try:
                j = int(i)
                scores += [j]
            except ValueError as e:
                argc -= 1
                print(f"Error: {e}")
                return
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}\n")


if __name__ == "__main__":
    ft_score_analytics()
