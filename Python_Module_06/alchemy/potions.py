try:
    from .elements import create_water, create_air, create_earth, create_fire

    def healing_potion() -> str:
        return (f"Healing potion brewed with {create_fire()} and "
                f"{create_water()}")

    def strength_potion() -> str:
        return (f"Strength potion brewed with {create_earth()} and"
                f" {create_fire()}")

    def invisibility_potion() -> str:
        return (f"Invisibility potion brewed with {create_air()} and "
                f"{create_water()}")

    def wisdom_potion() -> str:
        all_elements = f"{create_fire()}, {create_water()}, {create_earth()}, {create_air()}"
        return f"Wisdom potion brewed with all elements: {all_elements}"
except Exception as e:
    print(e)
