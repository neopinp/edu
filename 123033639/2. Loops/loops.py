"""
i = 0
while i < 2:
    print("Meow")
    i += 1 # i = i + 1
"""
"""
for _ in range(3):
    print("Meow")
"""
"""
while True:
    n = int(input("What's n?: "))
    if n > 0:
        break

for _ in range(n):
    print("Meow")
"""

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()

