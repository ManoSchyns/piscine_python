def input_temperature(temp_str: str) -> int:
    value: int = 0
    value = int(temp_str)
    return value


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    temp: int

    print("Input data is '25'")
    try:
        temp = input_temperature("25")
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)

    print("\nInput data is 'abc'")
    try:
        temp = input_temperature("abc")
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)

    print("\nAll tests completed - program didn’t crash!")


if __name__ == "__main__":
    test_temperature()
