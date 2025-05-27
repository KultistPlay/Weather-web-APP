from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__, template_folder="app/templates")

@app.route('/')
def main():
    return render_template("main.html")


@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    api_key = "2f074fd2995eed3456285ee96a418e28"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data['cod'] != 200:
            return render_template("main.html", error=data['message'])
            
        weather_info = {
            'city': data['name'],
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return render_template("main.html", weather=weather_info)
        
    except Exception as e:
        return render_template("main.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)