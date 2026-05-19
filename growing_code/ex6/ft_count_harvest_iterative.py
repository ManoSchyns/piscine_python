def ft_count_harvest_iterative() -> None:
    count: int = int(input("Days until harvest: "))
    i: int = 1
    while (i <= count):
        print("Day", i)
        i += 1
    print("Harvest time!")
