def convert(faces):
    faces = faces.replace(":)", "🙂")
    faces = faces.replace(":(", "🙁")
    return faces

def main():
    user_input = input(("ENTER A STRING WITH :) OR :( : "))
    user_input = convert(user_input)
    print(user_input)

main()



