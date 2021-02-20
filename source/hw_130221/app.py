import requests
import re


def main(*args, **kwargs) -> list:
    return re.findall(r'CTF{\w+}', requests.get('https://vk.com/wall-171787766_172').text)
