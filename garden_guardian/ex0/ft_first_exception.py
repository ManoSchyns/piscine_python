def input_temperature(temp_str: str) -> int:
    value: int = 0
    try:
        value = int(temp_str)
    except ValueError:
        print("Caught input_temperature error: " +
              "invalid literal for int() with base 10: " + temp_str)
    return value


def test_temperature() -> None:
    a: int
    print("=== Garden Temperature ===")
    try:
        print("\nInput data is '25'")
        a = input_temperature("25")
        if (a != 25):
            print("For input : '25' program return:", a)
        else:
            print("Temperature is now 25°C")

        print("\nInput data is '-25'")
        a = input_temperature("-25")
        if (a != -25):
            print("For input : '-25' program return:", a)
        else:
            print("Temperature is now -25°C")

        print("\nInput data is '2q'")
        a = input_temperature("2q")

        print("\nInput data is ''")
        a = input_temperature("")
    except Exception:
        print("===> Error <===")
        print("Program crashed")
        return
    print("\nAll tests completed - program didn’t crash!")
