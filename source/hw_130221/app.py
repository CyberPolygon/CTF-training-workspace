def main() -> list:
    html = requests.get('https://vk.com/wall-171787766_172', headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150', 'accept': '*/*'})
    match = list(set(re.findall(r"CTF\{\w*?}", html.text)))
    return match

print('test')