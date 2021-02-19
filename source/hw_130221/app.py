from requests import *
from re import *

def main() -> list:

    silka = get('https://vk.com/wall-171787766_172').text
    allresults = findall(r'CTF{[\d\w]*}', silka)

    return allresults
