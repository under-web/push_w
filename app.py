import time
import plyer
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_html(url):
    ua = UserAgent()
    headers = {'User-Agent': ua.firefox}
    res = requests.get(url, headers=headers)
    return res.text


def get_weather(res):
    soup = BeautifulSoup(res, 'lxml')
    block_w = soup.find('div', class_='tab_wrap')
    block_har = soup.find('div', class_='tab tooltip').get('data-text')
    time_w = block_w.find('div', class_="date xs fadeIn").text.strip()
    temp_w = block_w.find('span', class_="unit unit_temperature_c").text.strip()
    result_note = time_w + '\t' + temp_w + '\t' + block_har
    return result_note


def show_note(result_note):
    plyer.notification.notify(message=result_note,
                              app_name='wApp',
                              app_icon='1.ico',
                              title='Погода')


def main():
    while True:
        try:
            url = 'https://www.gismeteo.ru/weather-apastovo-204190/'
            show_note(get_weather(get_html(url)))
            time.sleep(3600)
        except Exception as e:
            time.sleep(10)


if __name__ == '__main__':
    main()
