# Create a list comprehension to calculate the leap years from 1588 to 2024.
# Take the hundred years rule and four hundred years rule into account

leap_years = [
    y for y in range(1588, 2024 + 1) if y % 4 == 0 and y % 100 != 0 or y % 400 == 0
]
print(leap_years)
