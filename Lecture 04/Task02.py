inches = float(input("enter inches (enter negative value to stop): "))

while inches >= 0:
    centimeters = inches * 2.54
    print(f"{inches} inches are {centimeters} centimeters")
    inches = float(input("Please enter inches (Enter negative value to stop): "))