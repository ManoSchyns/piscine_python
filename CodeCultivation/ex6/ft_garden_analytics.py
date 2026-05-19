class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self.stat: Plant.Stat = Plant.Stat()
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
        self.stat.add_number_age()

    def grow(self) -> None:
        to_grow: float
        if self.get_height() == 0.0:
            to_grow = 1.0
        else:
            to_grow = self.get_age() / self.get_height()
        self.set_height(self.get_height() + to_grow)
        self.stat.add_number_grow()

    def show(self) -> None:
        print(self._name.capitalize() + ":  ", end="")
        print(round(self._height, 1), end="")
        print("cm, ", end="")
        print(self._ages, end="")
        print(" days old")
        self.stat.add_number_show()

    @staticmethod
    def check_age(age_to_check: int) -> bool:
        if age_to_check >= 365:
            return True
        return False

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    # class statistiaue
    class Stat():

        def __init__(self) -> None:
            self._number_grow: int = 0
            self._number_age: int = 0
            self._number_show: int = 0

        def add_number_grow(self) -> None:
            self._number_grow += 1

        def add_number_age(self) -> None:
            self._number_age += 1

        def add_number_show(self) -> None:
            self._number_show += 1

        def get_number_grow(self) -> int:
            return self._number_grow

        def get_number_age(self) -> int:
            return self._number_age

        def get_number_show(self) -> int:
            return self._number_show

        def display(self) -> None:
            print(self.get_number_grow(), " grow, ",
                  self.get_number_age(), " age, ",
                  self.get_number_show(), " show", sep="")


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
        self.stat: Tree.Stat = Tree.Stat()

    def produce_shade(self) -> None:
        self._shade = True
        print("Tree " + self._name + " now produces a shade of ",
              round(self.get_height(), 1), "cm long and ",
              round(self._trunk_diameter, 1), "cm wide.", sep="")
        self.stat.add_number_shade()

    def show(self) -> None:
        super().show()
        print("Trunk diameter: ", round(self._trunk_diameter, 1), "cm", sep="")

    class Stat(Plant.Stat):

        def __init__(self):
            super().__init__()
            self._shade_count = 0

        def add_number_shade(self) -> None:
            self._shade_count += 1

        def get_number_shade(self) -> int:
            return self._shade_count

        def display(self) -> None:
            super().display()
            print(self.get_number_shade(), " shade", sep="")


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


class Seed(Flower):

    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age, color)
        self._seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = round(self._height * 2 / 3)

    def show(self) -> None:
        super().show()
        print("Seeds:", self._seeds)


def display_plant_stats(plant: Plant) -> None:
    print("Stats:  ", end="")
    plant.stat.display()


if __name__ == "__main__":

    print("=== Garden statistics ===")

    # =========================
    # CHECK AGE
    # =========================
    print("=== Check year-old")

    print("Is 30 days more than a year? ->",
          Plant.check_age(30))

    print("Is 400 days more than a year? ->",
          Plant.check_age(400))

    print()

    # =========================
    # FLOWER
    # =========================
    print("=== Flower")

    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_plant_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()

    rose.show()
    print("[statistics for Rose]")
    display_plant_stats(rose)

    print()

    # =========================
    # TREE
    # =========================
    print("=== Tree")

    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_plant_stats(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("[statistics for Oak]")
    display_plant_stats(oak)

    print()

    # =========================
    # SEED
    # =========================
    print("=== Seed")

    sunflower = Seed("sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[statistics for Sunflower]")
    display_plant_stats(sunflower)

    print("[make sunflower grow, age and bloom]")

    sunflower.grow()
    sunflower.age()
    sunflower.bloom()

    sunflower.show()
    print("[statistics for Sunflower]")
    display_plant_stats(sunflower)

    print()

    # =========================
    # ANONYMOUS
    # =========================
    print("=== Anonymous")

    unknown = Plant.create_anonymous()
    unknown.show()
    print("[statistics for Unknown plant]")
    display_plant_stats(unknown)
