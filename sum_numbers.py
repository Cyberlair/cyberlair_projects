def sum_numbers():
    numbers = []
    for i in range(6):
        while True:
            try:
                num = float(input(f"Enter number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Error: Please enter a valid number!")
    return sum(numbers)

try:
    total = sum_numbers()
    print(f"The sum of the numbers is: {total}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")