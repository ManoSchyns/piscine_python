class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.ages = age
        self.grown: float = 0.0

    def age(self) -> None:
        self.ages += 1

    def grow(self) -> None:
        to_grow: float = self.ages / self.height
        self.height += to_grow
        self.grown += to_grow

    def show(self) -> None:
        print(self.name.capitalize() + ":  ", end="")
        print(round(self.height, 1), end="")
        print("cm, ", end="")
        print(self.ages, end="")
        print(" days old")


if __name__ == "__main__":
    rose: Plant = Plant("rose", 25.0, 30)
    oak: Plant = Plant("oak", 200.0, 365)
    cactus: Plant = Plant("cactus", 5.0, 90)
    sunflower: Plant = Plant("sunflower", 80.0, 45)
    fern: Plant = Plant("fern", 15.0, 120)
    print("=== Plant Factory Output ===")
    print("Created:  ", end="")
    rose.show()
    print("Created:  ", end="")
    oak.show()
    print("Created:  ", end="")
    cactus.show()
    print("Created:  ", end="")
    sunflower.show()
    print("Created:  ", end="")
    fern.show()
