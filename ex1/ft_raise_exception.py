def input_temperature(temp_input: str) -> int:
    temperature = int(temp_input)
    if temperature >= 0 and temperature <= 40:
        return temperature
    if temperature > 40:
        raise ValueError(
            f'{temperature}°C is too hot for plants (max 40°C)'
            )
    raise ValueError(
        f'{temperature}°C is too cold for plants (min 0°C)'
        )


def test_temperature(temp_input: str) -> None:
    try:
        print(f"Input data is '{temp_input}'")
        temperature = input_temperature(temp_input)
        print(f"Temperature is now {temperature}°C\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")


def ft_raise_exception() -> None:
    valid_temperature = "25"
    invalid_temperature = "abc"
    hot_temperature = "100"
    cold_temperature = "-50"

    print("=== Garden Temperature Checker ===\n")

    test_temperature(valid_temperature)
    test_temperature(invalid_temperature)
    test_temperature(hot_temperature)
    test_temperature(cold_temperature)

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    ft_raise_exception()
