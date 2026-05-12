class GardenError(Exception):
    def __init__(self, error_mess="Unknown plant error"):
        super().__init__(error_mess)


class PlantError(GardenError):
    def __init__(self, error_mess="Unknown plant error"):
        super().__init__(error_mess)


class WaterError(GardenError):
    def __init__(self, error_mess="Unknown plant error"):
        super().__init__(error_mess)


def water_plant(plant_name: str) -> None:
    if (plant_name[0] < 'A' or plant_name[0] > 'Z'):
        raise PlantError("Invalid plant name to water: '" + plant_name + "'")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        print("Watering Tomato: [OK]")
        water_plant("Lettuce")
        print("Watering Lettuce: [OK]")
        water_plant("Carrots")
        print("Watering Carrots: [OK]")
    except PlantError as e:
        print("Caught PlantError: ", e)
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print()
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        print("Watering Tomato: [OK]")
        water_plant("lettuce")
        print("Watering Lettuce: [OK]")
        water_plant("carrots")
        print("Watering Carrots: [OK]")
    except PlantError as e:
        print("Caught PlantError: ", e)
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print()
    print("Cleanup always happens, even with errors!")
