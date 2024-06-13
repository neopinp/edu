# CREATING A FUNCTION

def main():
    name = input("What is your name?" )
    hello(name)

# main calls hello

def hello(to):
    print("Hello,",to) #name will pass through to and replace its value 

# hello calls main()
main()
