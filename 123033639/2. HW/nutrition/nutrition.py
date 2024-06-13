# outputs the number of calories in one portion of that fruit
# 20 fruits

fruits = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "grapes": "90",
    "honeydew": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "necatrine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "watermelon": "80"
}

user_fruit = input("What is the fruit name?: ").lower()
if user_fruit in fruits:
    print(f"Calories:",fruits[user_fruit])




