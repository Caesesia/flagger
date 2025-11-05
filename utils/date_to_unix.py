from datetime import datetime
import time

def convert_time(date_start: str, date_finish: str) -> int:

    ds = datetime.strptime(date_start, "%d/%m/%Y")
    df = datetime.strptime(date_finish, "%d/%m/%Y")

    return int(time.mktime(ds.timetuple())), int(time.mktime(df.timetuple()))
