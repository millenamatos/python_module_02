class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, message: str ="Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("\nTesting valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    finally:
        print("Closing watering system")
    print("\nTesting invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def ft_finally_block() -> None:
    print("=== Garden Watering System ===")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    ft_finally_block()
