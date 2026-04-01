def ft_analytics_dashboard() -> None:
    players: list[dict[str, int | str | bool | list[str]] | list[str]] = [
        {
            "name": "alice",
            "score": 2300,
            "level": 15,
            "region": "north",
            "active": True
        },
        {
            "name": "bob",
            "score": 1800,
            "level":  8,
            "region": "east",
            "active": True
        },
        {
            "name": "charlie",
            "score": 2150,
            "level": 12,
            "region": "central",
            "active": True
        },
        {
            "name": "diana",
            "score": 2050,
            "level": 11,
            "region": "north",
            "active": False
        }
    ]
    achievements: list[dict[str, str]] = [
        {"player": "alice", "achievement": "first_kill"},
        {"player": "alice", "achievement": "boss_slayer"},
        {"player": "alice", "achievement": "level_10"},
        {"player": "alice", "achievement": "speed_run"},
        {"player": "alice", "achievement": "untouchable"},
        {"player": "bob", "achievement": "first_kill"},
        {"player": "bob", "achievement": "level_10"},
        {"player": "bob", "achievement": "treasure_hunter"},
        {"player": "charlie", "achievement": "first_kill"},
        {"player": "charlie", "achievement": "boss_slayer"},
        {"player": "charlie", "achievement": "level_10"},
        {"player": "charlie", "achievement": "speed_run"},
        {"player": "charlie", "achievement": "untouchable"},
        {"player": "charlie", "achievement": "treasure_hunter"},
        {"player": "charlie", "achievement": "dragon_slayer"},
        {"player": "diana", "achievement": "first_kill"},
        {"player": "diana", "achievement": "level_10"},
    ]
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")

    high_score: list[str] = [p["name"] for p in players if p["score"] > 2000]
    print(f"High scorers (>2000): {high_score}")

    scores_doubled: list[int] = [p["score"] * 2 for p in players]
    print(f"Scores doubled: {scores_doubled}")

    active_users: list[str] = [p["name"] for p in players if p["active"]]
    print(f"Active players: {active_users}")

    print("\n=== Dict Comprehension Examples ===")

    player_score: dict[str, int] = {p["name"]: p["score"] for p in players}
    print(f"Player scores: {player_score}")

    score_catego: dict[str, int] = {
        "high": len([p for p in players if p["score"] > 2000]),
        "medium": len([p for p in players if 1800 < p["score"] <= 2000]),
        "low": len([p for p in players if p["score"] <= 1800])
    }
    print(f"Score categories: {score_catego}")
    achievement_counts = {
        p["name"]: len([c for c in achievements if c["player"] == p["name"]])
        for p in players
    }
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")
    unique_player: set[str] = {p["name"] for p in players}
    print(f"Unique players: {unique_player}")
    unique_achievement = {p["achievement"] for p in achievements}
    print(f"Unique achievements: {unique_achievement}")
    active_regions: set[str] = {p["region"] for p in players if p["active"]}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    totale_players: int = len(players)
    print(f"Total players: {totale_players}")
    print(f"Total unique achievements: {len(unique_achievement)}")
    average_score: float = sum(p["score"] for p in players) / totale_players
    print(f"Average score: {average_score}")
    # a = 1
    top_performer = players[0]
    for p in players:
        if p["score"] > top_performer["score"]:
            top_performer = p
    print(f"Top performer: {top_performer['name']} "
          f"({top_performer['score']} points, "
          f"{achievement_counts[top_performer['name']]} achievements)")


if __name__ == "__main__":
    ft_analytics_dashboard()
