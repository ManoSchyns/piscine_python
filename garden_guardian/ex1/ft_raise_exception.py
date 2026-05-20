def input_temperature(temp_str: str) -> int:
    value = int(temp_str)

    if value < 0:
        raise ValueError(f"{value}°C is too cold for plants (min 0°C)")

    if value > 40:
        raise ValueError(f"{value}°C is too hot for plants (max 40°C)")

    return value


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    try:
        print("\nInput data is '25'")
        input_temperature("25")
        print("Temperature is now 25°C")
    except ValueError as exception:
        print("Caught input_temperature error: ", exception)
    except Exception:
        print("===> Error <===")
        print("Program crashed")
        return

    try:
        print("\nInput data is 'abc'")
        input_temperature("abc")
    except ValueError as exception:
        print("Caught input_temperature error: ", exception)
    except Exception:
        print("===> Error <===")
        print("Program crashed")
        return

    try:
        print("\nInput data is '100'")
        input_temperature("100")
    except ValueError as exception:
        print("Caught input_temperature error: ", exception)
    except Exception:
        print("===> Error <===")
        print("Program crashed")
        return

    try:
        print("\nInput data is '-50'")
        input_temperature("-50")
    except ValueError as exception:
        print("Caught input_temperature error: ", exception)
    except Exception:
        print("===> Error <===")
        print("Program crashed")
        return

    print("\nAll tests completed - program didn’t crash!")


if __name__ == "__main__":
    test_temperature()
