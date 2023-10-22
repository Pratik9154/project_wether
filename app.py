from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/weatherapp',methods=['POST'])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"
    city=request.form.get('city')
    units=request.form.get('units')
    appid=request.form.get('appid')
    params ={
        'q': city,
        'units':units,
        'appid':appid
        }
    response = request.get(url,params=params)
    data = response.json()
    return f"data : {data}"


if __name__ == '__main__':
    app.run(host="0.0.0.0")