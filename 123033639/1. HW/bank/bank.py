
def main():
    greeting = input("Enter a greeting of choice: ").lower().strip()

    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

main()



