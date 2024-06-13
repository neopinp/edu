def main():
    camel_case = input("Input a camel case: ")
    snake_case = convert(camel_case)
    print("snake_case: ",snake_case)


def convert(phrase):
    new_phrase = ""
    for character in phrase:
        if character.isupper():
            new_phrase += "_" + character.lower()
        else:
            new_phrase += character
    return new_phrase

main()


