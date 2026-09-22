def main():
    s=input("What time is it? ").strip()
    hour=convert(s)
    if 7.0 <= hour <= 8.0:
        print("breakfast time")
    elif 12.0 <= hour <= 13.0:
        print("lunch time")
    elif 18.0 <= hour <= 19.0:
        print("dinner time")


def convert(time):
    hour_str,minute_str=time.split(":")
    hour=int(hour_str)
    minute=int(minute_str)
    return hour+(minute/60.0)


if __name__ == "__main__":
    main()