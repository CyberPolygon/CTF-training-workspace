import requests
import re


def main(*args, **kwargs) -> list:
    r = requests.get('https://vk.com/wall-171787766_172')
    return re.findall(r'CTF{\w+}', r.text)


