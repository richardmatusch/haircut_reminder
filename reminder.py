from win11toast import toast
from datetime import datetime, timedelta
import ephem

m = ephem.Moon()

def is_waxing(date_time):
    """determine if the moon is in waxing phase"""
    m.compute(date_time)
    moon_phase_now = m.phase

    m.compute(date_time + timedelta(hours=1))
    moon_phase_plus_one_hour = m.phase
    
    if moon_phase_plus_one_hour > moon_phase_now:
        return True


def find_match(date_time, operator, time_delta):
    """find and return closest date -1 timedelta where the moon is in waxing phase, and in leo constellation. you can go backwards or forwards from entered datetime value by selecting operator and increase precision with timedelta increment setting"""
    
    time_deltas = {
        'minutes': timedelta(minutes=1),
        'hours': timedelta(hours=1),
        'days': timedelta(days=1)
    }

    delta = time_deltas.get(time_delta) # get chosen time_delta

    found_match = ""
    while found_match == "":
        m.compute(date_time)
        constellation = ephem.constellation(m)
        moon_phase = m.phase
        if constellation[1] == "Leo" and (moon_phase > 0 and moon_phase < 100):
            found_match = date_time - delta # i am subtracting delta because i don't want to overshoot start of the window
        if operator == "+":
            date_time += delta
        elif operator == "-":
            date_time -= delta
    return found_match


def message():
    """message for the toast notification"""
    if time_till_window_start < timedelta(days=2) and window_start > current_date_time and is_waxing:
        return (f"Najbližší rastúci mesiac v levovi začne:\n{window_start.strftime('%d/%m/%Y o %H:%M')}")
    elif current_date_time >= window_start and current_date_time <= window_end:
        return (f"Mesiac rastie a je v levovi do:\n{window_end.strftime('%d/%m/%Y, %H:%M')}")

# calculations of needed values for notification
current_date_time = datetime.now() 
is_waxing = is_waxing(current_date_time)
window_start = find_match(find_match(find_match(current_date_time - timedelta(days=5), "+", "days"), "+", "hours"), "+", "minutes")
window_end = find_match(find_match(find_match(window_start + timedelta(days=5), "-", "days"), "-", "hours"), "-", "minutes")
time_till_window_start = window_start - current_date_time

message = message()

if message:
    # set the path for your icon...
    toast(message, icon=r'C:\path\to\your\icon\lion.png', scenario="incomingCall")


