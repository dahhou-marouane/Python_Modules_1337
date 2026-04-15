def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda a: a['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda a: ("* " + a + " *"), spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda a: a['power'])['power'],
        'min_power': min(mages, key=lambda a: a['power'])['power'],
        'avg_power': round(sum(map(lambda m: m['power'], mages))
                           / len(mages), 2)
    }


if __name__ == "__main__":

    artifacts = [
        {'name': 'Water Chalice', 'power': 63, 'type': 'relic'},
        {'name': 'Water Chalice', 'power': 104, 'type': 'accessory'},
        {'name': 'Crystal Orb', 'power': 86, 'type': 'armor'},
        {'name': 'Crystal Orb', 'power': 62, 'type': 'focus'}
        ]
    mages = [
        {'name': 'Ember', 'power': 63, 'element': 'water'},
        {'name': 'Riley', 'power': 52, 'element': 'shadow'},
        {'name': 'Kai', 'power': 65, 'element': 'wind'},
        {'name': 'Jordan', 'power': 86, 'element': 'shadow'},
        {'name': 'Casey', 'power': 59, 'element': 'water'}
        ]
    spells = ['tsunami', 'blizzard', 'earthquake', 'fireball']

    print("\nTesting artifact sorter...")
    sorter_artifact = artifact_sorter(artifacts)
    print(
        f"{sorter_artifact[0]['name']} ({sorter_artifact[0]['power']} "
        f"power) comes before {sorter_artifact[1]['name']} "
        f"({sorter_artifact[1]['power']} power)")

    print()

    print("Testing spell transformer...")
    for spell in spell_transformer(spells):
        print(spell, end=" ")
    print()

    filter_power = power_filter(mages, sorter_artifact[-1]['power'])
    stats_mage = mage_stats(mages)

    print("\nTesting power filter...")
    print(f"Mages with power >= {sorter_artifact[-1]['power']}:")
    for mage in filter_power:
        print(f"- {mage['name']} ({mage['power']})")

    print("\nTesting mage stats...")
    print(stats_mage)
