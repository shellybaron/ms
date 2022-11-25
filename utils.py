import datetime

def date_to_ts(date, format):
    return int(datetime.datetime.strptime(date, format).timestamp() * 1000)

def mill_to_years(time):
    return round(time / 1000 / 60 / 60 / 24 / 365)

def mill_to_month(time):
    return round(time / 1000 / 60 / 60 / 24)