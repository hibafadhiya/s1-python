def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

import datetime

current_year = datetime.datetime.now().year
final_year = int(input("Enter the final year: "))

print(f"Leap years from {current_year} to {final_year}:")

for year in range(current_year, final_year + 1):
    if is_leap_year(year):
        print(year)
