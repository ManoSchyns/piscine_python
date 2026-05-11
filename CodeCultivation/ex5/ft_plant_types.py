class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
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
        to_grow: float = self._ages / self._height
        self._height += to_grow

    def show(self) -> None:
        print(self._name.capitalize() + ":  ", end="")
        print(round(self._height, 1), end="")
        print("cm, ", end="")
        print(self._ages, end="")
        print(" days old")


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed: bool = False

    def bloom(self) -> None:
        if not self._bloomed:
            self._bloomed = True

    def show(self) -> None:
        super().show()
        print("Color :  " + self._color)
        if not self._bloomed:
            print(self._name.capitalize() + " has not bloomed yet")
        else:
            print(self._name.capitalize() + " is blooming beautifully!")


class Tree(Plant):

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        if trunk_diameter <= 0:
            print(self._name.capitalize() +
                  ":  Error, trunk diameter can’t be zero/negative")
            self._trunk_diameter = 1.0
        else:
            self._trunk_diameter = trunk_diameter
        self._shade = False

    def produce_shade(self) -> None:
        if not self._shade:
            self._shade = True
            print("[asking the " + self._name + " to produce shade]")
        else:
            print("Tree " + self._name + " now produces a shade of ",
                  round(self.get_height(), 1), "cm long and ",
                  round(self._trunk_diameter, 1), "cm wide.", sep="")

    def show(self) -> None:
        super().show()
        print("Trunk diameter: ", round(self._trunk_diameter, 1), "cm", sep="")


class Vegetable(Plant):

    def __init__(self, name: str, height: float,
                 age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print("Harvest season:  " + self._harvest_season)
        print("Nutritional value: ", self._nutritional_value)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose: Flower = Flower("rose", 15.0, 10, "red")
    rose.show()
    print("[asking the " + rose._name + " to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak: Tree = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato: Vegetable = Vegetable("tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(1, 21, 1):
        tomato.grow()
        tomato.age()
    tomato.show()
