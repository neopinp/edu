# 5, 10, 25 coins only - each bottle is 50 cents
# once the user inputs at least 50 cents, output how many cents the user is owed
# create one function to recieve the coin
# create one function to calculate the change/amount due and the amount owed to the customer


def get_coin():
    while True:
        try: # while true makes sure the loop doesnt end until the if statement is satisfied
            coin = int(input("Insert a coin: "))
            if coin in [5,10,25]:
                return coin
            else:
                print("Enter a 5,10,25 coin")
        except:
            print("Enter a valid coin integer")

def calculate_change(amount_due):
    while amount_due > 0:
        print("Amount Due:", amount_due)
        coin = get_coin()
        amount_due -= coin
# breaks out of the loop when amount_due > 0
    amount_owed = abs(amount_due)
    if amount_owed > 0:
        print("Amount owed:", amount_owed)
    else:
        print("No amount owed")

def main():
    amount_due = 50
    calculate_change(amount_due)

main()



