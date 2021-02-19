import requests
import re


def main() -> list:
    r = requests.get('https://vk.com/lifetrainings?w=wall-171787766_172')

    flags = re.findall( 'CTF{\w+}', r.text)

    with open('CTF.txt', "w", encoding="utf-8") as file:
	    for element in flags:
		    file.write(element+'\n')
    return flags
main()

