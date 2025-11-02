POUNDS_PER_TALENT = 20
LOTS_PER_POUND = 32
GRAMS_PER_LOT = 13.3

talents = float(input("How many talents would you like? \n"))
pounds = float(input("How many pounds would you like? \n"))
lots = float(input("How many lots would you like? \n"))

grams_from_talents = talents * POUNDS_PER_TALENT * LOTS_PER_POUND * GRAMS_PER_LOT
grams_from_pounds = pounds * LOTS_PER_POUND * GRAMS_PER_LOT
grams_from_lots = lots * GRAMS_PER_LOT

total_grams = grams_from_talents + grams_from_pounds + grams_from_lots

kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print("\nThe weight in modern units:" )
print(f"{kilograms} kilograms and {grams:.2f} grams.")
