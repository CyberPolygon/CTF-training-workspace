import requests
import re

def main() -> list:
    r = requests.get('https://vk.com/lifetrainings?w=wall-171787766_172')

    CTFka = re.findall( '[A-Z]\w\w[{]\w+[}]', r.text)

    File = open('CTF.txt', "w", encoding="utf-8")
    for element in CTFka:
         File.write(element)
         File.write('\n')
    File.close()
    return CTFka
main()
