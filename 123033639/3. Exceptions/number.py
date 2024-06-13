
def main():
    x = get_int("What's x?")
    print(f"x is {x}")


def get_int(prompt):
    while True: # continuously asks for an integer (try statement)
        try:
            return int(input(prompt))
            #break can be placed here
        except ValueError:
            pass # doesnt print an erorr message
        
main()
