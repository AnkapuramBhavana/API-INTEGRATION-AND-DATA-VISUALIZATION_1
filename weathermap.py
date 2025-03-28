import requests
import matplotlib.pyplot as plt

api_key = "0c28cf60d00b28be508c492663948973"  
city = "Bangalore"

url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&cnt=5&appid={api_key}"


response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    
    
    times = [item['dt_txt'] for item in data['list']]
    temperatures = [item['main']['temp'] for item in data['list']]
    
    
    plt.figure(figsize=(10, 5))
    plt.plot(times, temperatures, marker='s', color='red')
    plt.title(f"Temperature Forecast for {city}")
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)  
    plt.grid(True)
    plt.tight_layout()
    
    
    plt.show()

else:
    print(f"Error: {response.status_code}")
