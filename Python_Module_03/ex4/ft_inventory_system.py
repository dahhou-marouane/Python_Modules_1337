import sys


def ft_inventory_system() -> None:
    argc = len(sys.argv)
    totale_items = 0
    count = 0
    if argc == 1:
        print("Error: No enough args\nExample Usage: $> python3 "
              "ft_inventory_system.py sword:1 potion:5 shield:2 "
              "armor:3 helmet:1")
        return
    inventory: dict[str, int] = {}
    for i in sys.argv[1:]:
        try:
            key, value = i.split(":")
            if not key:
                raise ValueError(f" with the arg {key}:{value}")
            value = int(value)
            totale_items += value
        except ValueError as e:
            print(f"Error: {e}\nInput should be like sword:1 as single arg")
            return
        if key in inventory:
            inventory[key] += value
        else:
            inventory[key] = value
    for i in inventory.keys():
        count += 1
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {totale_items}")
    print(f"Unique item types: {count}")
    print("\n=== Current Inventory ===")
    copy_dict: dict[str, int] = dict(inventory)
    i = 0
    max_key = ""
    while i < len(copy_dict):
        max = -1
        for key, value in copy_dict.items():
            if value > max:
                max = value
                max_key = key
        if copy_dict.get(max_key) > 1:
            print(
                f"{max_key}: {copy_dict.get(max_key)} units "
                f"({(max * 100) / totale_items:.1f}%)")
        else:
            print(
                f"{max_key}: {copy_dict.get(max_key)} unit "
                f"({(max * 100) / totale_items:.1f}%)")
        copy_dict[max_key] = 0
        i += 1
    print("\n=== Inventory Statistics ===")
    max = -1
    for key, value in inventory.items():
        if value > max:
            max = value
            max_key = key
    min = max
    min_key = ""
    for key, value in inventory.items():
        if value <= min:
            min = value
            min_key = key
    print(f"Most abundant: {max_key} ({inventory.get(max_key)} units)")
    print(f"Least abundant: {min_key} ({inventory.get(min_key)} unit)")
    print("\n=== Item Categories ===")
    moderate: dict[str, int] = {}
    scarce: dict[str, int] = {}
    restock: str = ""
    for key, value in inventory.items():
        if value > 4:
            moderate.update({key: value})
        else:
            scarce.update({key: value})
            if value < 2:
                if restock == "":
                    restock = key
                else:
                    restock += ", " + key

    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")
    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {restock}")
    print("\n=== Dictionary Properties Demo ===")
    Dictionary_keys: str = ""
    Dictionary_values: str = ""
    for key, value in inventory.items():
        if Dictionary_keys == "":
            Dictionary_keys = key
        else:
            Dictionary_keys += ", " + key
        if Dictionary_values == "":
            Dictionary_values = str(value)
        else:
            Dictionary_values += ", " + str(value)
    print(f"Dictionary keys: {Dictionary_keys}")
    print(f"Dictionary values: {Dictionary_values}")
    lookup = "sword"
    print(
        f"Sample lookup - '{lookup}' in inventory: "
        f"{bool(inventory.get(lookup))}")


if __name__ == "__main__":
    ft_inventory_system()
