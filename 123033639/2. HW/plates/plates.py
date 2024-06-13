# start with two letters
# max of 6 character minimum of 2 characters
# numbers must come at the end of the plate, and the first number cannot be 0
# no periods, spaces, or punctuation marks allowed
# lists can be split eg: s[0:2] of CS50 = CS


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
     if check_start(s) and check_numbers(s) and length_check(s):
         return True
     return False

# check if beginning starts with letters
def check_start(plate):
    if plate[0:2].isalpha():
        return True
    return False


#2-6 characters
def length_check(plate):
    if 2 <= len(plate) <=6 and plate.isalnum():
        return True
    return False

#check if letters follow digits, and check if numbers start with 0
def check_numbers(plate):
    for index, char in enumerate(plate):
        if char.isdigit():
            if char == '0' or plate[index:].isalpha():
                return False
            break
    return True 


main()
