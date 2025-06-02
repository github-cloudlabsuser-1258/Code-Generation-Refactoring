# A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases

MAX = 100

def calculate_sum(arr: list[int]) -> int:
    """Return the sum of a list of integers."""
    return sum(arr)

def get_number_of_elements() -> int:
    """Prompt the user for the number of elements, ensuring it's valid."""
    while True:
        try:
            n = int(input(f"Enter the number of elements (1-{MAX}): "))
            if 1 <= n <= MAX:
                return n
            print(f"Invalid input. Please enter a number between 1 and {MAX}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_integer_inputs(n: int) -> list[int]:
    """Prompt the user to enter n integers, ensuring all are valid."""
    arr = []
    count = 0
    while count < n:
        try:
            value = int(input(f"Enter integer #{count + 1}: "))
            arr.append(value)
            count += 1
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return arr

def main() -> None:
    try:
        n = get_number_of_elements()
        arr = get_integer_inputs(n)
        total = calculate_sum(arr)
        print("Sum of the numbers:", total)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
