import requests
import re

def get_flags() -> list:
    request = requests.get('https://vk.com/wall-171787766_172')

    searchFlags = re.findall('[C,С][T,Т]F\{[a-z,A-Z,0-9,а-я,А-Я]{1,}\}', request.text)
    if not searchFlags:
        print('Флаги не обнаружены')
    else:
        return searchFlags
    return []

if __name__ == '__main__':
    print(get_flags())