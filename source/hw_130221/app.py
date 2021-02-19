import requests
import re


def main():
	response = requests.get('https://vk.com/lifetrainings?w=wall-171787766_172')
	return re.findall(r'CTF{\w+}', response.text)
