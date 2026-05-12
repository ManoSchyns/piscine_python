def ft_count_harvest_recursive():
    count = int(input("Days until harvest:  "))

    def helper(i, max):
        if (i > max):
            print("Harvest time!")
            return
        print("Day", i)
        i += 1
        helper(i, max)

    helper(1, count)
