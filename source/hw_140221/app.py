def main() -> list:
    html = requests.get('https://vk.com/lifetrainings', headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150', 'accept': '*/*'})
    match = re.findall(r"CTF\{\w*?}", html.text)
    return match
