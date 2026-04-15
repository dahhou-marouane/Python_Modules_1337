if __name__ == "__main__":
    try:
        from alchemy.grimoire.validator import validate_ingredients
        from alchemy.grimoire.spellbook import record_spell
        print("\n=== Circular Curse Breaking ===\n")
        print("Testing ingredient validation:")
        print('validate_ingredients("fire air"):',
              validate_ingredients("fire air"))
        print('validate_ingredients("dragon scales"):',
              validate_ingredients("dragon scales"))

        print()
        print("Testing spell recording with validation:")
        print('record_spell("Fireball", "fire air"):',
              record_spell("Fireball", "fire air"))
        print('record_spell("Dark Magic", "shadow"):',
              record_spell("Dark Magic", "shadow"))

        print()
        print("Testing late import technique:")
        print('record_spell("Lightning", "air"):',
              record_spell("Lightning", "air"))

        print()
        print('Circular dependency curse avoided using late imports!')
        print('All spells processed safely!')
    except Exception as e:
        print(e.__class__.__name__, e)
