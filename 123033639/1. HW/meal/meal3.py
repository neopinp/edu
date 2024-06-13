def main():
    time = input("What time is it?: ")
    new_time = convert(time)
    if 7.00 <= new_time <= 8.00:
        print("breakfast time")
    elif 12.00 <= new_time <= 13.00:
        print("lunch time")
    elif 18.00 <= new_time <= 19.00:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    new_hours = float(hours)
    minutes = int(minutes)
    new_minutes = float((f"{minutes / 60:,.2f}"))
    new_time = new_hours + new_minutes
    return new_time


if __name__ == "__main__":
    main()

