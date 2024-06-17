from win11toast import toast
from datetime import datetime, timedelta
import ephem

def find_match(time, operator, time_delta):
    """find and return closest date where moon constellation is leo and in waxing phase. you can go backwards or forwards from entered datetime value by selecting operator and increase precision with timedelta increment setting"""
    m = ephem.Moon()
    
    time_deltas = {
        'minutes': timedelta(minutes=1),
        'hours': timedelta(hours=1),
        'days': timedelta(days=1)
    }

    delta = time_deltas.get(time_delta) # get chosen time_delta

    found_match = ""
    while found_match == "":
        m.compute(time)
        constellation = ephem.constellation(m)
        moon_phase = m.phase
        if constellation[1] == "Leo" and (moon_phase > 0 and moon_phase < 50):
            found_match = time - delta # i am subtracting delta because i don't want to overshoot start of the window
        if operator == "+":
            time += delta
        elif operator == "-":
            time -= delta
    return found_match


def message():
    """message for the ephem notification. this is only very rough function and needs to be worked on more"""
    if current_time < window_start:
        return (f"not a good time for a haircut\nnext window will start in: {time_till_window_start}\non: {window_start}")
    elif current_time >= window_start:
        return (f"moon is in leo and it is growing!\nyou can cut your hair till {window_end}, which is {remaining_window}")

# calculations of needed values for notification
current_time = datetime.now()
window_start = find_match(find_match(find_match(current_time, "+", "days"), "+", "hours"), "+", "minutes")
print(window_start)
window_end = find_match(find_match(find_match(window_start + timedelta(days=5), "-", "days"), "-", "hours"), "-", "minutes")
remaining_window = window_end - current_time
time_till_window_start = window_start - current_time

message = message()
# toast(message)
print(message)


 