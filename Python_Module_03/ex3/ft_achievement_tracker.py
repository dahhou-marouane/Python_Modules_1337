def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")
    alice: set[str] = {'first_kill', 'level_10',
                       'treasure_hunter', 'speed_demon'}
    bob: set[str] = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie: set[str] = {'level_10', 'treasure_hunter',
                         'boss_slayer', 'speed_demon', 'perfectionist'}
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {bob.union(alice, charlie)}")
    print(f"Total unique achievements: {len(bob.union(alice, charlie))}\n")
    print(f"Common to all players: {alice.intersection(bob, charlie)}")
    rare = (alice.difference(charlie, bob) | charlie.difference(
        alice, bob) | bob.difference(charlie, alice))
    print(f"Rare achievements (1 player): {rare}\n")
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    ft_achievement_tracker()
