# year = 2026

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(year," is a leap year ")
# else:
#     print(year," not a leap year ")


year = 2023

if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
    print( year, "year is leap year")
else:
    print(year,"not a leap year")

