from flask import Flask, render_template, request
from weather import get_current_weather, get_lat_lon
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv('API_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form.get('city_name')
        state_code = request.form.get('state_code')
        country_code = request.form.get('country_code')
        lat, lon, city_name, country_name = get_lat_lon(city_name, state_code, country_code, API_KEY)
        weather_data = get_current_weather(lat, lon, API_KEY)
        weather_data.city_name = city_name
        weather_data.country_name = country_name
        return render_template('index.html', weather_data=weather_data)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
