"""
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
"""
# extensions.py
# extensions.py

def main():
    name = input("What is the name of the file?: ").strip().lower()

    if name.endswith(".gif"):
        print("image/gif", end="")
    elif name.endswith(".jpg"):
        print("image/jpg", end="")
    elif name.endswith(".jpeg"):
        print("image/jpeg", end="")
    elif name.endswith(".png"):
        print("image/png", end="")
    elif name.endswith(".pdf"):
        print("application/pdf", end="")
    elif name.endswith(".txt"):
        print("text/plain", end="")
    elif name.endswith(".zip"):
        print("application/zip", end="")
    else:
        print("application/octet-stream", end="")

main()





