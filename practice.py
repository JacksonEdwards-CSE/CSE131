
# def get_prefix():
#     gender = input("Are you male or female? ")
#     return ("Mr." if gender == 'm' else "Mrs.")

# def main():
#     name = input("What is your last name? ")
#     prefix = get_prefix()
#     print(f"Hello, {prefix} {name}.")

# def main():
#     year = 2026

#     birth_year = int(input("What year were you born? "))

#     print(f"You will turn {year - birth_year} this year.")

# def get_temperature():
#     far_temp = int(input("Give me a temp: "))
#     return far_temp

# def convert(far_temp):
#     cel_temp = (far_temp - 32) * 5 / 9
#     return cel_temp

# def display(cel_temp):
#     print(cel_temp)

# def main():
#     far_temp = get_temperature()

#     cel_temp = convert(far_temp)

#     display(cel_temp)

def get_type():
    unit_type = input("Enter the unit of the temperature: ")

    return unit_type

def get_temp():
    temp = float(input("Enter the temperature: "))
    return temp

def convert_to_kelvin(temp, unit_type):
    if unit_type == "f":
        kelvin = (temp - 32) * 5 / 9 + 273.15
    
    else:
        kelvin = temp + 273.15
    
    return kelvin
    
def convert_to_farenheight(temp, unit_type):
    if unit_type == "k":
        far = (temp - 273.15) * 9/5 + 32
    else:
        far = (temp *9/5 ) + 32

    return far
    
def convert_to_celcius(temp, unit_type):
    if unit_type == "k":
        cel = temp - 273.15
    else:
        cel = (temp - 32) * 5/9

    return cel
    
def display_temps(kelvin, far, cel):
    print(f"Kelvin: {kelvin}\nFarenheight: {far}\nCelcius: {cel}")

def main():
    unit_type = get_type()
    temp = get_temp()

    match unit_type:

        case "k":
            kelvin = temp

            far = convert_to_farenheight(temp, unit_type)

            cel = convert_to_celcius(temp, unit_type)
        
        case "f":
            kelvin = convert_to_kelvin(temp, unit_type)

            far = temp

            cel = convert_to_celcius(temp, unit_type)
        
        case "c":
            kelvin = convert_to_kelvin(temp, unit_type)

            far = convert_to_farenheight(temp, unit_type)

            cel = temp
    
    display_temps(kelvin, far, cel)

main()