import requests
import re

def main():
    URL = "https://vk.com/lifetrainings?w=wall-171787766_172"
    responce = requests.get(URL).text

    x = r"CTF{\w*}"
    return re.findall(x, responce)
print(main())