# 5, 10, 25 coins only - each bottle is 50 cents
# once the user inputs at least 50 cents, output how many cents the user is owed

amount_due = 50

while amount_due > 0:
    print("Amount Due:", amount_due)
    coin = int(input("Insert coin: "))

    if coin in [5,10,25]:
        amount_due -= coin
    else:
        ("enter a valid coin")

if amount_due < 0:
    change_owed = abs(amount_due)
    print("Change Owed:",change_owed)
else:
    print("Change Owned:",amount_due)




