import requests
import emoji
from PIL import Image
from random import randrange, choice

API='9438af37542bfc5371506eabe0b0df54'
#city=input().strip().lower() - если вдруг надо будет город искать


def get_weather(limit):
    string=''
    emoji_list = {'ясно': ':sun:',
                  'облачно с прояснениями': ':sun_behind_cloud:',
                  'переменная облачность': ':sun_behind_cloud:',
                  'пасмурно': ':cloud:',
                  'небольшая облачность': ':cloud:',
                  'небольшой дождь': ':cloud_with_rain:',
                  'дождь': ':cloud_with_rain:',
                  'гроза': ':cloud_with_lighting_and_rain:',
                  'снег': 'cloud_with_snow',
                  'туман': ':fog:'}
    data_var=''
    count=0
    list_day=('Сегодня:', '\nЗавтра:', '\nПослезавтра:', '\nПослепослезавтра:', '\nПослепослепослезавтра:', '\nПослепослепослепослезавтра:')

    while True:
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                               params={'id': 499099, 'units': 'metric', 'lang': 'ru', 'APPID': API})
            break
        except Exception as e:
            print("Exception (forecast):", e)

    data=res.json()

    for i in data['list']:
        try:
            emoji_weather = emoji.emojize(emoji_list[i['weather'][0]['description']])
        except:
            emoji_weather = i['weather'][0]['description']

        if i['dt_txt'][:10]!=data_var:
            data_var=i['dt_txt'][:10]
            if count>=limit:
                break
            string += list_day[count] + '\n'
            count += 1
        string+=i['dt_txt'][11:16]+'   ' +emoji_weather+ '    ' +'{0:+3.0f}'.format(i['main']['temp'])+'\n'


    return  string

def get_mem():
    mem_id = randrange(0, 147)
    #file_way=f'C:/meme_repository/{str(mem_id)}.jpg'
    #file = Image.open(file_way)
    file_way = f'https://disk.yandex.ru/d/n4-DHhTmpbNxpw/{mem_id}.jpg'
    res = requests.get(file_way)
    #data = res.json()

    return res

def main():
    print(get_mem())

def get_stick():
    stick_lib=['CAACAgIAAxkBAAEM8IlnBdR2rGtI8ZeyyRlxMhjtLwGb8QACrh8AAjjk6ErCNiNfNrdhgjYE',
               'CAACAgIAAxkBAAIFAAFnTsC1qdMc7_ywbaHsW7GKonU39wACMFkAAj_18ElgD1i1hfv5_zYE',
               'CAACAgIAAxkBAAIFAAFnTsC1qdMc7_ywbaHsW7GKonU39wACMFkAAj_18ElgD1i1hfv5_zYE',
               'CAACAgIAAxkBAAIFAAFnTsC1qdMc7_ywbaHsW7GKonU39wACMFkAAj_18ElgD1i1hfv5_zYE',
               'CAACAgIAAxkBAAIEKWdOsyem_s0K-mIO7tzh0q-fYs1cAALvIAACf-roSoRTS-P5ETh2NgQ',
               'CAACAgIAAxkBAAIEOGdOt0PO_PjFBl2TLPJdGPoFEwyKAAKTGwACVoFBSYxpB21uy7wjNgQ',
               'CAACAgIAAxkBAAIEPGdOt21LiM-qOPKyJ4gNRX8qLpnVAALnXwACK1-JSSekYSKGJ4vINgQ',
               'CAACAgIAAxkBAAIEPmdOt3mqqQPOfATLX5tfqkyOGgABxQAC31gAAoFuQUnztCJHwbGgVzYE',
               'CAACAgIAAxkBAAIEQGdOt5yLJTIAAbo0n2YgAlpmeoODRgACXFQAAvx0AUrhIUerG3RcyDYE',
               'CAACAgIAAxkBAAIEQmdOt6z_A5VTpmrlizkBa5yT32a0AAI8YwAC07sQSjXMcD3c9tOkNgQ',
               'CAACAgIAAxkBAAIERGdOt7lmSvsik4ZZIG0yAdzIeh0VAAKFYAACrcohSucB_qS5I4UPNgQ',
               'CAACAgIAAxkBAAEM8IlnBdR2rGtI8ZeyyRlxMhjtLwGb8QACrh8AAjjk6ErCNiNfNrdhgjYE',
               'CAACAgIAAxkBAAIEKWdOsyem_s0K-mIO7tzh0q-fYs1cAALvIAACf-roSoRTS-P5ETh2NgQ'
               'CAACAgIAAxkBAAIEOGdOt0PO_PjFBl2TLPJdGPoFEwyKAAKTGwACVoFBSYxpB21uy7wjNgQ',
               'CAACAgIAAxkBAAIEPGdOt21LiM-qOPKyJ4gNRX8qLpnVAALnXwACK1-JSSekYSKGJ4vINgQ',
               'CAACAgIAAxkBAAIEPmdOt3mqqQPOfATLX5tfqkyOGgABxQAC31gAAoFuQUnztCJHwbGgVzYE',
               'CAACAgIAAxkBAAIEQGdOt5yLJTIAAbo0n2YgAlpmeoODRgACXFQAAvx0AUrhIUerG3RcyDYE',
               'CAACAgIAAxkBAAIEQmdOt6z_A5VTpmrlizkBa5yT32a0AAI8YwAC07sQSjXMcD3c9tOkNgQ',
               'CAACAgIAAxkBAAIERGdOt7lmSvsik4ZZIG0yAdzIeh0VAAKFYAACrcohSucB_qS5I4UPNgQ',
               'CAACAgIAAxkBAAEM8IlnBdR2rGtI8ZeyyRlxMhjtLwGb8QACrh8AAjjk6ErCNiNfNrdhgjYE',
               'CAACAgIAAxkBAAIEKWdOsyem_s0K-mIO7tzh0q-fYs1cAALvIAACf-roSoRTS-P5ETh2NgQ'
               'CAACAgIAAxkBAAIEOGdOt0PO_PjFBl2TLPJdGPoFEwyKAAKTGwACVoFBSYxpB21uy7wjNgQ',
               'CAACAgIAAxkBAAIEPGdOt21LiM-qOPKyJ4gNRX8qLpnVAALnXwACK1-JSSekYSKGJ4vINgQ',
               'CAACAgIAAxkBAAIEPmdOt3mqqQPOfATLX5tfqkyOGgABxQAC31gAAoFuQUnztCJHwbGgVzYE',
               'CAACAgIAAxkBAAIEQGdOt5yLJTIAAbo0n2YgAlpmeoODRgACXFQAAvx0AUrhIUerG3RcyDYE',
               'CAACAgIAAxkBAAIEQmdOt6z_A5VTpmrlizkBa5yT32a0AAI8YwAC07sQSjXMcD3c9tOkNgQ',
               'CAACAgIAAxkBAAIERGdOt7lmSvsik4ZZIG0yAdzIeh0VAAKFYAACrcohSucB_qS5I4UPNgQ'
               ]
    return choice(stick_lib)

if __name__ == '__main__':
    main()