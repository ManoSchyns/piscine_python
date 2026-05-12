def input_temperature(temp_str: str) -> int:
    value: int = 0
    try:
        value = int(temp_str)
    except ValueError:
        print("Caught input_temperature error: " +
              "invalid literal for int() with base 10: " + temp_str)
    if (value < 0 or value > 40):
        raise ValueError("Temperature is invalid. The plants die")
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
    except ValueError as exception:
        print("Caught input_temperature error: ", exception)
    except Exception:
        print("===> Error <===")
        print("Program crashed")
        return

    try:
        print("\nInput data is '2q'")
        a = input_temperature("2q")
    except ValueError as exception:
        print("Caught input_temperature error: ", exception)
    except Exception:
        print("===> Error <===")
        print("Program crashed")
        return

    try:
        print("\nInput data is ''")
        a = input_temperature("")
    except ValueError as exception:
        print("Caught input_temperature error: ", exception)
    except Exception:
        print("===> Error <===")
        print("Program crashed")
        return

    try:
        print("\nInput data is '2q'")
        a = input_temperature("2q")
    except ValueError as exception:
        print("Caught input_temperature error: ", exception)
    except Exception:
        print("===> Error <===")
        print("Program crashed")
        return

    try:
        print("\nInput data is '100'")
        a = input_temperature("100")
    except ValueError as exception:
        print("Caught input_temperature error: ", exception)
    except Exception:
        print("===> Error <===")
        print("Program crashed")
        return

    try:
        print("\nInput data is '-50'")
        a = input_temperature("-50")
    except ValueError as exception:
        print("Caught input_temperature error: ", exception)
    except Exception:
        print("===> Error <===")
        print("Program crashed")
        return

    print("\nAll tests completed - program didn’t crash!")


if __name__ == "__main__":
    test_temperature()
