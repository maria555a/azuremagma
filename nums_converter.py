seconds = int(input("Enter an amount of seconds: "))
if 0 <= seconds < 8640000:
    day_seconds = 24 * 60 * 60
    hour_seconds = 60 * 60
    minute_seconds = 60

    days, rest = divmod(seconds, day_seconds)
    hours, rest = divmod(rest, hour_seconds)
    minutes, secs = divmod(rest, minute_seconds)
    hours_str = str(hours).zfill(2)
    minutes_str = str(minutes).zfill(2)
    seconds_str = str(secs).zfill(2)

    if days == 1:
        day_str = "1 day"
    elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
        day_str = f"{days} days"
    elif days % 10 == 1 and days % 100 != 11:
        day_str = f"{days} day"
    else:
        day_str = f"{days} days"

    print(f"{day_str}, {hours_str}: {minutes_str}: {seconds_str}")

