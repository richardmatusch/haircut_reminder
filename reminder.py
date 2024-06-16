from win11toast import toast
from datetime import datetime, timedelta
import ephem

def find_match(time, operator):
    m = ephem.Moon()
    found_match = ""
    while found_match == "":
        m.compute(time)
        constellation = ephem.constellation(m)
        moon_phase = m.phase
        if constellation[1] == "Leo" and (moon_phase > 0 and moon_phase < 50):
            found_match = time
        if operator == "+":
            time += timedelta(minutes=1)
        elif operator == "-":
            time -= timedelta(minutes=1)
    return found_match

def message():
    if current_time < window_start:
        print(f"not a good time for a haircut\nnext window will start in: {time_till_window_start}")
    elif current_time >= window_start:
        print(f"moon is in leo and it is growing!\n you can cut your hair till {window_end}, which is {remaining_window}")

current_time = datetime.now()
window_start = find_match(current_time, "+")
window_end = find_match(window_start + timedelta(days=5), "-")
remaining_window = window_end - current_time
time_till_window_start = window_start - current_time

message()




 