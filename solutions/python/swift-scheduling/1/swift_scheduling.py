from datetime import datetime, timedelta


def delivery_date(start, description):
    # Parse input timestamp string
    start = datetime.fromisoformat(start)
    desc = description.strip().upper()

    # Helpers
    def is_workday(d):
        return d.weekday() < 5

    def iso(dt):
        return dt.strftime("%Y-%m-%dT%H:%M:%S")

    def first_workday_of_month(year, month):
        d = datetime(year, month, 1, 8, 0)
        while not is_workday(d):
            d += timedelta(days=1)
        return d

    def last_workday_of_quarter(year, quarter):
        end_month = quarter * 3
        # First day of next month → step back
        if end_month == 12:
            d = datetime(year, 12, 31, 8, 0)
        else:
            d = datetime(year, end_month + 1, 1, 8, 0) - timedelta(days=1)
        while not is_workday(d):
            d -= timedelta(days=1)
        return d

    wd = start.weekday()  # Monday = 0
    hour = start.hour

    # ---------- FIXED ----------
    if desc == "NOW":
        return iso(start + timedelta(hours=2))

    if desc == "ASAP":
        if hour < 13:
            return iso(start.replace(hour=17, minute=0, second=0, microsecond=0))
        tomorrow = start + timedelta(days=1)
        return iso(tomorrow.replace(hour=13, minute=0, second=0, microsecond=0))

    if desc == "EOW":
        if wd <= 2:  # Mon–Wed
            diff = 4 - wd
            d = start + timedelta(days=diff)
            return iso(d.replace(hour=17, minute=0, second=0, microsecond=0))
        # Thu–Fri (or weekend) → Sunday 20:00
        diff = 6 - wd
        d = start + timedelta(days=diff)
        return iso(d.replace(hour=20, minute=0, second=0, microsecond=0))

    # ---------- VARIABLE ----------
    if desc.endswith("M") and desc[:-1].isdigit():
        N = int(desc[:-1])
        if start.month < N:
            year = start.year
        else:
            year = start.year + 1
        return iso(first_workday_of_month(year, N))

    if desc.startswith("Q") and desc[1:].isdigit():
        N = int(desc[1:])
        current_quarter = (start.month - 1) // 3 + 1
        if current_quarter <= N:
            year = start.year
        else:
            year = start.year + 1
        return iso(last_workday_of_quarter(year, N))

    raise ValueError("invalid delivery date description")

