class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(self.name.capitalize() + ":  ", end="")
        print(self.height, end="")
        print("cm, ", end="")
        print(self.age, end="")
        print(" days old")


if __name__ == "__main__":
    rose: Plant = Plant("rose", 25, 30)
    sunflower: Plant = Plant("sunflower", 80, 45)
    cactus: Plant = Plant("cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()
