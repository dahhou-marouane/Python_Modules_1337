if __name__ == "__main__":
    try:
        import alchemy.elements
        from alchemy.elements import create_fire
        from alchemy.potions import healing_potion as heal
        from alchemy.elements import create_fire, create_water
        from alchemy.potions import strength_potion

        print("\n=== Import Transmutation Mastery ===\n")

        print("Method 1 - Full module import:")
        print("alchemy.elements.create_fire(): ", end="")
        print(alchemy.elements.create_fire())

        print()
        print("Method 2 - Specific function import:")
        print("create_water(): ", end="")
        print(create_water())

        print()
        print("Method 3 - Aliased import:")
        print("heal(): ", end="")
        print(heal())

        print()
        print("Method 4 - Multiple imports:")
        print("create_earth(): ", end="")
        print(alchemy.elements.create_earth())
        print("create_fire(): ", end="")
        print(create_fire())
        print("strength_potion(): ", end="")
        print(strength_potion())

        print("\nAll import transmutation methods mastered!")
    except Exception as e:
        print(e.__class__.__name__, e)
