"""
x = float(input("What is x? "))
y = float(input("What is y? "))

z = round(x + y) # round to nearest integer
print(f"{z:,}") # print with commas every 3 digits
"""

# round(number[, ndigits])
# round(x + y, 2) to two digits
# X = 999
# Y = 1

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def main1():
    y = int(input("What's y? "))
    print("y squared is", square(y))

def square(n): # square will pass any variables into n and square, x = n, y = n
    return pow(n, 2) #first = value, second = power digit

main() # calls x
main1() # calls y
