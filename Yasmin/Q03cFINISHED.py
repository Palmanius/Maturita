# Q03c

# Input requested
year = int(input("Enter a year in this format YYYY e.g. 2000: "))

# Process input and display the result
# Add your code here
def CheckLeap(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print ('This is a leap year')
    else: 
        print ("This is not a leap year")

CheckLeap(year)