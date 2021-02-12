# BeautifulSoup testing environment because parsing is hard

import requests
from bs4 import BeautifulSoup


BASE_URL = {
    'fe6': 'https://serenesforest.net/binding-blade/',
    'fe7': 'https://serenesforest.net/blazing-sword/',
    'fe8': 'https://serenesforest.net/the-sacred-stones/',
}


response = requests.get(BASE_URL['fe6'] + 'characters/recruitment/')
content = response.content
soup = BeautifulSoup(content, features='html.parser')
characters = soup.find_all('tr')

def construct(data) -> dict:
    ret = {}

    for arr in data:
        arr = arr.text.split('\n')

        if len(arr) < 6:
            character = arr[1]
            recruitment = arr[3]
        else:
            character = arr[1]
            recruitment = arr[4]

        ret[character] = recruitment

    return ret

d = construct(characters[1:])

print(d)
