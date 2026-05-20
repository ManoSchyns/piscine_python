class GardenError(Exception):
    def __init__(self, error_mess="Unknown garden error"):
        super().__init__(error_mess)


class PlantError(GardenError):
    def __init__(self, error_mess="Unknown plant error"):
        super().__init__(error_mess)


class WaterError(GardenError):
    def __init__(self, error_mess="Unknown water error"):
        super().__init__(error_mess)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError("Invalid plant name to water: '" + plant_name + "'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print("Caught PlantError:", e)
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print()
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("carrots")
    except PlantError as e:
        print("Caught PlantError:", e)
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
