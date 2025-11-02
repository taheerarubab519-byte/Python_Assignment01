import random
digit_1 = random.randint(0,9)
digit_2 = random.randint(0,9)
digit_3 = random.randint(0,9)

code_3_digit = f"{digit_1} {digit_2} {digit_3}"

digit_4 = random.randint(1, 6)
digit_5 = random.randint(1, 6)
digit_6 = random.randint(1, 6)
digit_7 = random.randint(1, 6)

code_4_digit = f"{digit_4} {digit_5} {digit_6} {digit_7}"

print("Generated Combination of Codes")
print(f"3-digit code (0-9): {code_3_digit}")
print(f"4-digit code (1-6): {code_4_digit}")
