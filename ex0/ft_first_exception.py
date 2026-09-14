def input_temperature(temp_input):
    return int(temp_input)


def test_temperature(temp_input):
    try:
        print(f"Input data is '{temp_input}'")
        temperature = input_temperature(temp_input)
        print(f"Temperature is now {temperature}°C\n")
    except ValueError as error:
        print(error, "\n")


def ft_first_exception():
    valid_temperature = "25"
    invalid_temperature = "abc"
    print("=== Garden Temperature ===\n")
    test_temperature(valid_temperature)
    test_temperature(invalid_temperature)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    ft_first_exception()
