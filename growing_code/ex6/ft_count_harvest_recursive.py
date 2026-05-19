def ft_count_harvest_recursive() -> None:
    count: int = int(input("Days until harvest: "))

    def helper(i: int, max: int) -> None:
        if (i > max):
            print("Harvest time!")
            return
        print("Day", i)
        i += 1
        helper(i, max)

    helper(1, count)
