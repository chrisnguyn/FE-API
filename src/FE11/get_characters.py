import requests
from bs4 import BeautifulSoup


def execute():
    response = requests.get('https://serenesforest.net/awakening/characters/recruitment/main-story/')
    content = response.content
    soup = BeautifulSoup(content, features='html.parser')
    characters = soup.find_all('tr')

    character_list = {}

    for character in characters[1:]:
        data = character.text.split('\n')
        k = data[1]
        v = (data[3], data[4])
        character_list[k] = v

    return character_list
