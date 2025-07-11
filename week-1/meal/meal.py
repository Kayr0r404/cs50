# python3


def main():
    time = input("what time is it? ").strip()
    num = convert(time)
    if num >= 7 and num <= 8:
        print("breakfast time")
    elif num >= 12 and num <= 13:
        print("lunch time")
    elif num >= 18 and num <= 19:
        print("dinner time")


def convert(time):
    time = time.split(":")
    return int(time[0]) + (int(time[1]) / 60)


if __name__ == "__main__":
    main()
