def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    valid_temperature = "25"
    print(f"Input data is '{valid_temperature}'")
    try:
        temperature = input_temperature(valid_temperature)
        print(f"Temperature is now {temperature}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print()

    invalid_temperature = "abc"
    print(f"Input data is '{invalid_temperature}'")
    try:
        temperature = input_temperature(invalid_temperature)
        print(f"Temperature is now {temperature}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print()


if __name__ == "__main__":
    test_temperature()
    print("All tests completed - program didn't crash!")
