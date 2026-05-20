class GardenError(Exception):
    def __init__(self, error_mess="Unknown garden error"):
        super().__init__(error_mess)


class PlantError(GardenError):
    def __init__(self, error_mess="Unknown plant error"):
        super().__init__(error_mess)


class WaterError(GardenError):
    def __init__(self, error_mess="Unknown water error"):
        super().__init__(error_mess)


def raise_error(name: str, water: int, numbe_plants: int) -> None:
    error: str
    if (name == "go"):
        raise GardenError()
    elif (name != "carrot" and name != "salade"):
        error = "The " + name + " plant is wilting!"
        raise PlantError(error)
    elif (water < 3):
        error = "Not enough water in the tank!"
        raise WaterError(error)
    elif (water > 20):
        error = "Too much water in the tank!"
        raise WaterError(error)
    elif (numbe_plants > 40):
        raise GardenError("The garden is full")


def test_error_class() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    try:
        raise_error("tomato", 7, 10)
    except PlantError as e:
        print("Caught PlantError:", e)
    print()

    print("Testing WaterError..")
    try:
        raise_error("carrot", 0, 10)
    except WaterError as e:
        print("Caught WaterError:", e)
    print()

    print("Testing catching all garden errors...")
    try:
        raise_error("tomato", 7, 10)
    except GardenError as e:
        print("Caught GardenError:", e)

    try:
        raise_error("carrot", 0, 10)
    except GardenError as e:
        print("Caught GardenError:", e)

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_error_class()
