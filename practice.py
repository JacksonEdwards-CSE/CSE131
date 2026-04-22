
# def Get_Prefix():
#     gender = input("Are you male or female? ")
#     return ("Mr." if gender == 'm' else "Mrs.")

# def Main():
#     name = input("What is your last name? ")
#     prefix = Get_Prefix()
#     print(f"Hello, {prefix} {name}.")

def Main():
    year = 2026

    birth_year = int(input("What year were you born? "))

    print(f"You will turn {year - birth_year} this year.")

Main()