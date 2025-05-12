from flask import Flask, render_template, request, redirect, url_for
import sys
import os

# Add the parent directory to sys.path to import get_demerit_points
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from functions import get_demerit_points

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        driving_speed_str = request.form.get('driving_speed', '').strip()
        speed_limit = request.form.get('speed_limit', '').strip()
        
        # Check for missing values
        if not driving_speed_str and not speed_limit:
            result = {'error': 'Please enter a driving speed and speed limit.'}
        elif not driving_speed_str:
            result = {'error': 'Please enter a driving speed.'}
        elif not speed_limit:
            result = {'error': 'Please enter a speed limit.'}
        else:
            try:
                # Determine if driving speed was entered as integer
                driving_speed_float = float(driving_speed_str)
                driving_speed_int = int(driving_speed_float)
                driving_speed_display = driving_speed_int if driving_speed_float == driving_speed_int else driving_speed_float
                driving_speed = driving_speed_float  # for calculation
                
                # Speed limit must be integer
                speed_limit = int(speed_limit)
                holiday_period = 'holiday_period' in request.form
                
                mandatory, points = get_demerit_points(driving_speed, speed_limit, holiday_period)
                
                # Add message for not speeding case
                if points == 0:
                    result = {
                        'info': f'Driving at {driving_speed_display}km/h in a {speed_limit}km/h zone is not speeding.'
                    }
                else:
                    result = {
                        'mandatory': mandatory,
                        'points': points,
                        'driving_speed': driving_speed_display,
                        'speed_limit': speed_limit,
                        'holiday_period': holiday_period,
                        'message': (
                            f'Driving at {driving_speed_display}km/h in a {speed_limit}km/h zone '
                            f'is '
                            f' {points} points.'
                        )
                    }
            except ValueError:
                result = {'error': 'Please enter valid numbers'}
            
    return render_template('index.html', result=result)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
