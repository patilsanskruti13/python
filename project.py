import datetime

# Problem 1: Computing the number of days in a month
def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month
      
    Returns:
      The number of days in the input month.
    """
    if month == 12:
        next_month = datetime.date(year + 1, 1, 1)
    else:
        next_month = datetime.date(year, month + 1, 1)
    current_month = datetime.date(year, month, 1)
    delta = next_month - current_month
    return delta.days


# Problem 2: Checking if a date is valid
def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day
      
    Returns:
      True if year-month-day is a valid date and False otherwise
    """
    if not (datetime.MINYEAR <= year <= datetime.MAXYEAR):
        return False
    if not (1 <= month <= 12):
        return False
    if not (1 <= day <= days_in_month(year, month)):
        return False
    return True


# Problem 3: Computing the number of days between two dates
def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date
      
    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is before the first date.
    """
    if not (is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2)):
        return 0
    
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)
    
    if date2 < date1:
        return 0
    
    delta = date2 - date1
    return delta.days


# Problem 4: Calculating a person's age in days
def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day
      
    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input date is in the future.
    """
    if not is_valid_date(year, month, day):
        return 0
    
    today = datetime.date.today()
    birthday = datetime.date(year, month, day)
    
    if birthday > today:
        return 0
    
    return (today - birthday).days


# Example Usage
if __name__ == "__main__":
    print("Days in Feb 2024:", days_in_month(2024, 2))  # Leap year
    print("Is 2023-02-29 valid?", is_valid_date(2023, 2, 29))
    print("Days between 2023-01-01 and 2023-01-31:", days_between(2023, 1, 1, 2023, 1, 31))
    print("Age in days for someone born on 2000-01-01:", age_in_days(2000, 1, 1))
