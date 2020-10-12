
# pip install matplotlib
# pip install requests
# pip install bs4

import matplotlib.pyplot as plt
import requests
from requests import ReadTimeout, HTTPError, Timeout, ConnectionError
from bs4 import BeautifulSoup
from datetime import date

try:

    country = input("Type in the name of the country : ")
    url = f"https://www.worldometers.info/coronavirus/country/{country.lower()}/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    data = soup.find_all("div", class_="maincounter-number")
    cases = data[0].text.strip()
    deaths = data[1].text.strip()
    recovered = data[2].text.strip()
except (HTTPError, ReadTimeout, Timeout, ConnectionError):
    print('*** Something is wrong with your connection ***')

except:
    print("*** The country might not exist. ***")
else:
    
    x_axis = ['Coronavirus cases', 'Deaths', 'Recovered']
    y_axis = [cases, deaths, recovered]
    y_axis = [int(i.replace(',', '')) for i in y_axis] #converting string data to int

    plt.style.use('dark_background')
    plt.title(f'Coronavirus in {country.upper()} on {date.today()}')
    chart = plt.bar(x_axis, y_axis)
    chart[0].set_color('yellow') #cases bar
    chart[1].set_color('crimson') #deaths bar
    chart[2].set_color('lawngreen') #recovered bar

    for idx, rect in enumerate(chart):
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2 ,height+10,y_axis[idx], ha='center', va='bottom')


    plt.show()


