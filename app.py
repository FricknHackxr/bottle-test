from bottle import Bottle, run, template, static_file
import ephem
from datetime import datetime

app = Bottle()

@app.route('/')
def index():
    moon = ephem.Moon()
    moon.compute()
    moon_phase = round(moon.phase)
    moon_phase_angle = moon_phase * 3.6  # 360 degrees / 100%
    moon_phase_text = get_moon_phase_text(moon_phase)
    return template('index.html', moon_phase=moon_phase, moon_phase_angle=moon_phase_angle, moon_phase_text=moon_phase_text)

def get_moon_phase_text(moon_phase):
    if moon_phase == 0:
        return "New Moon"
    elif 0 < moon_phase <= 25:
        return "Waxing Crescent"
    elif moon_phase == 25:
        return "First Quarter"
    elif 25 < moon_phase < 50:
        return "Waxing Gibbous"
    elif moon_phase == 50:
        return "Full Moon"
    elif 50 < moon_phase < 75:
        return "Waning Gibbous"
    elif moon_phase == 75:
        return "Last Quarter"
    elif 75 < moon_phase < 100:
        return "Waning Crescent"
    else:
        return "Unknown"

# Starte den Bottle-Server
if __name__ == '__main__':
    run(app, host='localhost', port=8080)

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

run(app, host='localhost', port=8080)
