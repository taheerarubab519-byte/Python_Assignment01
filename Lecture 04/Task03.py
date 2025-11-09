numbers = []
while True:
    user_data = input("Please enter a number (leave blank to stop): ")

    if user_data == "":
        break
    try:
        num = float(user_data)
        numbers.append(num)
    except ValueError:
        print("Please enter a valid number.")

if numbers:
    smallest_no = min(numbers)
    largest_no = max(numbers)
    print(f"\nThe smallest number is: {smallest_no}")
    print(f"The largest number is: {largest_no}")
else:
    print("\nNo numbers were entered.")