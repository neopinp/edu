# start with two letters
# max of 6 character minimum of 2 characters
# numbers must come at the end of the plate, and the first number cannot be 0
# no periods, spaces, or punctuation marks allowed

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#check start of the plate
def check_start(plate):
    if plate[0:2].isalpha():
        return True
    return False


#check length of the plate
def check_length(plate):
    if 2 <= len(plate) <= 6 and plate.isalnum():
        return True
    return False

#iterate through the string and check until you find a digit
# then check if the digit is 0 and if the following characters are digits
def check_numbers(plate):
    for index, character in enumerate(plate):
        if character.isdigit():
            if plate[index] == '0' or not plate[index:].isdigit():
                return False
            break
    return True


def is_valid(s):
    if check_length(s) and check_numbers(s) and check_start(s) == True:
        return True
    return False





main()
