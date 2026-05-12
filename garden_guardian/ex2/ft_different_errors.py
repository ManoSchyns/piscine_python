def garden_operations(operation_number: int) -> None:
    a: str
    if operation_number == 0:
        int("abs")
    elif operation_number == 1:
        4 / 0
    elif operation_number == 2:
        open("blabl")
    elif operation_number == 3:
        a = 9 + "emf"
    return

def test_error_types():
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    try:
        garden_operations(0)
    except ValueError as exception:
        print("Caught ValueError: ", exception)
    print("Testing operation 1...")
    try:
        garden_operations(1)
    except ZeroDivisionError as exception:
        print("Caught ZeroDivisionError: ", exception)

    print("Testing operation 2...")
    try:
        garden_operations(2)
    except FileNotFoundError as exception:
        print("Caught FileNotFoundError: ", exception)

    print("Testing operation 3...")
    try:
        garden_operations(3)
    except TypeError as exception:
        print("Caught TypeError: ", exception)

    print("Testing operation 4...")
    try:
        garden_operations(4)
        print("Operation completed successfully")
    except Exception as exception:
        print("Caught ValueError: ", exception)
    
    print("\nAll error types tested successfully!")
