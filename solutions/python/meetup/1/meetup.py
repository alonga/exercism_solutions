from datetime import date, timedelta


class MeetupDayException(ValueError):
    """Custom exception for invalid meetup date requests."""
    pass


WEEKDAY_MAP = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}


def meetup(year, month, week, day_of_week):
    if day_of_week not in WEEKDAY_MAP:
        raise MeetupDayException("Invalid weekday name.")

    target_wday = WEEKDAY_MAP[day_of_week]

    first_day = date(year, month, 1)
    first_wday_offset = (target_wday - first_day.weekday()) % 7
    first_occurrence = first_day + timedelta(days=first_wday_offset)

    if week == "teenth":
        d = date(year, month, 13)
        while d.day <= 19:
            if d.weekday() == target_wday:
                return d
            d += timedelta(days=1)
        raise MeetupDayException("That day does not exist.")

    if week == "last":
        if month == 12:
            d = date(year + 1, 1, 1) - timedelta(days=1)
        else:
            d = date(year, month + 1, 1) - timedelta(days=1)
        while d.month == month:
            if d.weekday() == target_wday:
                return d
            d -= timedelta(days=1)
        raise MeetupDayException("That day does not exist.")

    # Numerical weeks
    week_map = {
        "first": 0,
        "second": 1,
        "third": 2,
        "fourth": 3,
        "fifth": 4,
    }

    if week not in week_map:
        raise MeetupDayException("Invalid week descriptor.")

    occurrence = first_occurrence + timedelta(days=7 * week_map[week])
    if occurrence.month != month:
        raise MeetupDayException("That day does not exist.")

    return occurrence
