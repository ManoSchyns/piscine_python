class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._grown: float = 0.0
        if height < 0:
            print(self._name.capitalize() +
                  ":  Error, height can’t be negative")
            self._height = 1.0
        else:
            self._height = height
        if age < 0:
            print(self._name.capitalize() +
                  ":  Error, age can’t be negative")
            self._ages = 0
        else:
            self._ages = age

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(self._name.capitalize() +
                  ":  Error, age can’t be negative")
            print("Age update rejected")
        else:
            self._ages = new_age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(self._name.capitalize() +
                  ":  Error, height can’t be negative")
            print("Height update rejected")
        else:
            self._height = new_height

    def get_age(self) -> int:
        return self._ages

    def get_height(self) -> float:
        return self._height

    def age(self) -> None:
        self._ages += 1

    def grow(self) -> None:
        to_grow: float
        if self._height == 0.0:
            to_grow = 1.0
        else:
            to_grow = self._ages / self._height
        self._height += to_grow
        self._grown += to_grow

    def show(self) -> None:
        print(self._name.capitalize() + ":  ", end="")
        print(round(self._height, 1), end="")
        print("cm, ", end="")
        print(self._ages, end="")
        print(" days old")


if __name__ == "__main__":
    rose: Plant = Plant("rose", 25.0, 10)
    print("Plant created:  ", end="")
    rose.show()
    rose.set_height(25)
    rose.set_age(30)
    print("\nHeight updated:  ", round(rose.get_height(), 1), "cm", sep="")
    print("Age updated: ", rose.get_age(), " days", sep="")
    print("\n", end="")
    rose.set_age(-1)
    rose.set_height(-1)
    print("\nCurrent state:  ", end="")
    rose.show()
