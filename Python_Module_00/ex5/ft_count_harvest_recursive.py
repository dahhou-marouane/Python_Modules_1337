def ft_count_harvest_recursive() -> None:
    harvest = int(input('Days until harvest: '))

    def helper(i: int, harvest: int) -> None:
        if (i == harvest):
            print('Harvest time!')
            return None
        print(f"Day {i}")
        helper(i + 1, harvest)
    helper(1, harvest + 1)
