age = input("What's your age?\n")

life_expectancy = 90
years_left = life_expectancy - int(age)
years_left_inWeeks = years_left * 52

print(f"You have {years_left_inWeeks} weeks left.")