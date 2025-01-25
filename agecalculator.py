from datetime import datetime,timedelta

# Loop to collect date of birth inputs
for n in range(3):  # Loops over 0, 1, 2
    if n == 0:
        d = {'date': int(input("Enter the date in which you were born: "))}  # Day
    elif n == 1:
        m = {'month': int(input("Enter the month in which you were born (as a number): "))}  # Month
    elif n == 2:
        y = {'year': int(input("Enter the year in which you were born: "))}  # Year

# Extract values from dictionaries
date = d['date']
month = m['month']
year = y['year']

# Create a date of birth using the collected values
dob = datetime(year, month, date)

# Calculate the current date
current_date = datetime.now()

# Calculate the years
yearsold = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))

# Calculate the months
if current_date.month > dob.month:
    monthsold = current_date.month - dob.month
else:
    monthsold = 12 + current_date.month - dob.month
if monthsold == 12 :
    yearsold=yearsold+1
    monthsold=0


# Adjust months if the current day is less than the birth day
if current_date.day < dob.day:
    monthsold -= 1

# Calculate the days
if current_date.day >= dob.day:
    daysold = current_date.day - dob.day
else:
    # Get the last day of the previous month
    last_day_previous_month = (current_date.replace(day=1) - timedelta(days=1)).day
    daysold = last_day_previous_month - dob.day + current_date.day

# Print the result
print(f"Your date of birth is: {dob.strftime('%d/%m/%Y')}")

print(f"Your exact age is: {yearsold} years, {monthsold} months, and {daysold} days.")
