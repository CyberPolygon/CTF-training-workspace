import requests
import re

def main() -> list:
    requestvk = requests.get('https://vk.com/lifetrainings?w=wall-171787766_172', headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150', 'accept': '*/*'})
    ctfflags = list(set(re.findall(r'CTF\{\w*?}', requestvk.text)))

    file = open('CTF_1.txt', "w")
    for element in ctfflags:
        file.write(element)
        file.write('\n')
    file.close()
    return ctfflags

main()
