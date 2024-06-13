# 5, 10, 25 coins only - each bottle is 50 cents
# once the user inputs at least 50 cents, output how many cents the user is owed

def get_coin(): # loops continuously but only loops when called by get_coin() until 5,10, or 25 is entered
    while True:
        try:
            coin = int(input("Insert coin: "))
            if coin in [5,10,25]:
                return coin
            else:
                print("Enter a dime, nickel, or quarter")
        except: # checks if anything other than an integer is inputted
            print("Enter a valid number")

def calculate_change(amount_due): # this function has the ability to check the amount due and the amount owed at the end because of abs()
    while amount_due > 0:
        print("Amount due: ", amount_due)
        coin = get_coin()
        amount_due -= coin

    change_owed = abs(amount_due)
    if change_owed > 0:
        print("Change owed:",change_owed)
    else:
        print("No change owed.")

def main():
    amount_due = 50
    calculate_change(amount_due)



main()


