from datetime import date, timedelta
import ephem

# nejaka forma upozornenia every day, bud strihaj, alebo nestrihaj - zobraz najblizsi datum.

today = date.today()
tomorrow = today + timedelta(days=1)

def check_constellation(day):
    m = ephem.Moon()
    m.compute(day)
    constellation = ephem.constellation(m)
    moon_phase = m.phase
    print(moon_phase)
    if constellation[1] == "Leo":
        print("strihaj")
        return True
    else:
        print("nestrihaj")
        return False

check_constellation(tomorrow)


