# 1. Name:
#      Jackson Edwards
# 2. Assignment Name:
#      Lab 03: Calendar
# 3. Assignment Description:
#      Display a calendar of the month the user inputs aligning with the days of the year.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was getting the display_calendar() function working. I had to figure out
#      how to get the blank spaces to print properly and how to get it you start a new line at
#      the end of the week.
# 5. How long did it take for you to complete the assignment?
#      2 hours

def display_calendar(calendar):

    print(calendar[0])
    print(calendar[1], end="")

    for date in range(len(calendar)):
        
        if date + 3 < len(calendar):
            print(calendar[date + 3], end="")

        if (date + calendar[2]) % 7 == 6:
            print("|")

def create_calendar(month, day, is_leap):

    if is_leap:
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31]
    else:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31]

    week_days = ["", "|    ", "|    |    ", "|    |    |    ", "|    |    |    |    ", 
                 "|    |    |    |    |    ", "|    |    |    |    |    |    "]

    calendar = ["| Su | Mo | Tu | We | Th | Fr | Sa |"]

    calendar.append(week_days[day % 7])
    calendar.append(day)


    for date in range(days_in_month[month - 1]):
        
        date +=1

        if date < 10:
            date_string = f"| 0{date} "
        else:
            date_string = f"| {date} "
        
        calendar.append(date_string)
    
    return calendar

def get_start_week_day(end_year, month, is_leap):

    total_days = 0

    for year in range(1753, end_year):

        if year % 400 == 0:
            total_days += 366

        elif year % 4 == 0 and year % 100 != 0:
            total_days += 366

        else:
            total_days += 365

    days_to_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    days_to_month_leap = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 365]

    if is_leap:
        total_days += days_to_month_leap[month - 1]

    else:
        total_days += days_to_month[month - 1]


    start_week_day = (total_days + 1) % 7

    return start_week_day

def get_is_leap(year):

    if year % 400 == 0:
        is_leap = True

    elif year % 4 == 0 and year % 100 != 0:
        is_leap = True

    else:
        is_leap = False

    return is_leap

def get_user_input():
    done = True

    while done:

        try:
            month = int(input("Enter a month (MM):"))
            
            if month < 1 or month > 12:
                print("Please enter a valid month. (1-12)\n")
            else:
                done = False

        except (TypeError, ValueError):
            print("please enter a valid month number.\n")
        
    while not done:

        try:
            year = int(input("Enter a year (YYYY): "))

            if year < 1753:
                print("Please enter a valid year. (1753 or later)\n")
            else:
                done = True

        except (TypeError, ValueError):
            print("please enter a valid year number.\n")
        
    return year, month

def main():

    year, month = get_user_input()

    is_leap = get_is_leap(year)

    start_week_day = get_start_week_day(year, month, is_leap)

    calendar = create_calendar(month, start_week_day, is_leap)

    display_calendar(calendar)

if __name__ == "__main__":
    main()