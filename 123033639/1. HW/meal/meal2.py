def main():
    time_input = input("What time is it?: ")
    time = convert(time_input)
    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    #turn hours into a float and minutes / 60 into a float with two decimals
    return round(float(hours) + float(minutes / 60, 2))


if __name__ == "__main__":
    main()

