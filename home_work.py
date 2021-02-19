import requests
import re

def get_html(url):
    content=requests.get(url).text
    return content

def flag_finder(content,mask):
    pattern = re.compile(mask)
    return pattern.findall(content)

def main():
    url = 'https://vk.com/lifetrainings?w=wall-171787766_172'
    pattern = r'(CTF{[a-z|A-z|0-9]*})'
    file = open('flags.txt','w')
    flags = flag_finder(get_html(url),pattern)
    for i in flags: file.write(i + '\n')
    return flag_finder(get_html(url),pattern)

if __name__ == '__main__':
    main()