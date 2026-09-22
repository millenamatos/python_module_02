def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(temp_str: str) -> None:
    try:
        print(f"Input data is '{temp_str}'")
        temperature = input_temperature(temp_str)
        print(f"Temperature is now {temperature}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print()


def ft_first_exception() -> None:
    valid_temperature = "25"
    invalid_temperature = "abc"
    print("=== Garden Temperature ===\n")
    test_temperature(valid_temperature)
    test_temperature(invalid_temperature)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    ft_first_exception()
