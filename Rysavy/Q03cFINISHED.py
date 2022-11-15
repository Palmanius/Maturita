# Q03c

# Input requested
year = int(input("Enter a year in this format YYYY e.g. 2000: "))

# Process input and display the result
# Add your code here

if year % 400 == 0:
    print(year, "is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")