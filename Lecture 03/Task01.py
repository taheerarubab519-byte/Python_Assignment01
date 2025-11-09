length = float(input("Enter the length of zander in centimeters: "))
legal_limit_size = 42

if length >= legal_limit_size:
    shortfall = legal_limit_size - length
    print(f"The zander is {shortfall:.1f} cm below the legal size limit. Please release it back into the lack.")

else:
    print("The zander meets the size limit and can be kept.")