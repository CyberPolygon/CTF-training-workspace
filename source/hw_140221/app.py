import requests
import re

def main() -> list:
    requestvk = requests.get('https://vk.com/lifetrainings?w=wall-171787766_172')
    ctfflags = re.findall( '\w\w\w[{]\w+[}]', requestvk.text)

    file = open('CTF_1.txt', "w")
    for element in ctfflags:
        file.write(element)
        file.write('\n')
    file.close()
    return ctfflags

main()
