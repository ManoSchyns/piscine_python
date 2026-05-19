class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.ages = age
        self.grown: float = 0.0

    def age(self) -> None:
        self.ages += 1

    def grow(self) -> None:
        to_grow: float
        if self.height == 0.0:
            to_grow = 1.0
        else:
            to_grow = self.ages / self.height
        self.height += to_grow
        self.grown += to_grow

    def show(self) -> None:
        print(self.name.capitalize() + ":  ", end="")
        print(round(self.height, 1), end="")
        print("cm, ", end="")
        print(self.ages, end="")
        print(" days old")


if __name__ == "__main__":
    plant: Plant = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    plant.show()
    i: int = 1

    while i <= 7:
        print("=== Day", i, "===")
        plant.grow()
        plant.age()
        plant.show()
        i += 1
    print("Growth this week:  ", round(plant.grown, 1), "cm", sep="")
