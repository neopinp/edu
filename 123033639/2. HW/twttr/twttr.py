# prompt user for a string - output string with ommitted vowels whether lowercase or uppercase

def remove_vowels(phrase):
    new_phrase = ""
    vowels = "aeiouAEIOU"
    for character in phrase:
        if character not in vowels:
            new_phrase += character
    return new_phrase



def main():
    phrase = input("Enter a string that will have all vowels removed: ")
    print(remove_vowels(phrase))

main()

