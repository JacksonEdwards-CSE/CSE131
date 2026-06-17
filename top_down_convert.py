
def get_number():

    number = -1
    
    while number < 0:

        try:
            
            number = int(input("what is the decimal number? "))
            print()

        except ValueError:

            print("\nPlease enter a positive integer number.\n")
            
            number = -1
            

    return number

def convert_to_binary(number):

    if number == 0:
        return '0'

    binary_digits = []

    while number > 0:

        binary_digits.append(number % 2)

        number //= 2

    binary_string = ''

    for i in range(len(binary_digits)-1, -1, -1):

        binary_string += str(binary_digits[i])
    
    return binary_string

def convert_to_octal(number):
    if number == 0:
        return '0'

    octal_digits = []

    while number > 0:

        octal_digits.append(number % 8)

        number //= 8

    octal_string = ''

    for i in range(len(octal_digits)-1, -1, -1):

        octal_string += str(octal_digits[i])
    
    return octal_string

def convert_to_hex(number):
    if number == 0:
        return '0'

    hex_digits = []

    while number > 0:

        hex_digits.append(number % 16)

        number //= 16

    hex_string = ''

    for i in range(len(hex_digits)-1, -1, -1):

        if hex_digits[i] > 9:

            hex_letters = ['A', 'B', 'C', 'D', 'E', 'F']

            hex_string += hex_letters[hex_digits[i] - 10]
        
        else:
            hex_string += str(hex_digits[i])
    
    return hex_string

def convert(number):

    '''Call functions to convert the number into 
    Binary, Octal, and Hexadecimal'''

    binary = convert_to_binary(number)

    octal = convert_to_octal(number)

    hex = convert_to_hex(number)

    return binary, octal, hex

def display_numbers(user_number, binary_number, octal_number, hex_number):

    print(f"Decimal: {user_number}, Binary: {binary_number}, Octal: {octal_number}, Hexadecimal: {hex_number}")

def test_binary():
    assert convert_to_binary(0) == '0'
    assert convert_to_binary(1) == '1'
    assert convert_to_binary(5) == '101'
    assert convert_to_binary(10) == '1010'
    assert convert_to_binary(15) == '1111'
    assert convert_to_binary(16) == '10000'
    assert convert_to_binary(255) == '11111111'
    assert convert_to_binary(256) == '100000000'
    print('All Binary tests have passed.')
    return

def test_octal():
    assert convert_to_octal(0) == '0'
    assert convert_to_octal(1) == '1'
    assert convert_to_octal(5) == '5'
    assert convert_to_octal(10) == '12'
    assert convert_to_octal(15) == '17'
    assert convert_to_octal(16) == '20'
    assert convert_to_octal(255) == '377'
    assert convert_to_octal(256) == '400'
    print('All Octal tests have passed.')

def test_hex():
    assert convert_to_hex(0) == '0'
    assert convert_to_hex(1) == '1'
    assert convert_to_hex(5) == '5'
    assert convert_to_hex(10) == 'A'
    assert convert_to_hex(11) == 'B'
    assert convert_to_hex(12) == 'C'
    assert convert_to_hex(13) == 'D'
    assert convert_to_hex(14) == 'E'
    assert convert_to_hex(15) == 'F'
    assert convert_to_hex(16) == '10'
    assert convert_to_hex(255) == 'FF'
    assert convert_to_hex(256) == '100'
    print('All Hex tests have passed.')

def test_runner():
    '''Run all test functions'''

    test_binary()

    test_octal()

    test_hex()

    return

def main():

    test_runner()

    number = get_number()

    bin, oct, hex = convert(number)

    display_numbers(number, bin, oct, hex)

if __name__ == "__main__":
    main()