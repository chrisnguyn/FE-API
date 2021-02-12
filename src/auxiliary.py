import requests
from bs4 import BeautifulSoup


BASE_URL = {
    'fe6': 'https://serenesforest.net/binding-blade/',
    'fe7': 'https://serenesforest.net/blazing-sword/',
    'fe8': 'https://serenesforest.net/the-sacred-stones/',
}


def get_characters(game: str) -> dict:  # probably need gam specific functions since different table lengths on SF.net
    response = requests.get(BASE_URL[game] + 'characters/recruitment/')
    content = response.content
    soup = BeautifulSoup(content, features='html.parser')
    characters = soup.find_all('tr')
    character_list = {}

    for character in characters[1:]:
        data = character.text.split('\n')
        k = data[1]

        if len(data) < 6:
            v = data[3]
        else:
            v = data[4]

        character_list[k] = v

    return character_list


def get_stats(game: str, name: str) -> dict:
    def generate(data):
        return {
            'Character' : data[1],
            'Health' : data[2],
            'Str / Mag' : data[3],
            'Skill' : data[4],
            'Speed' : data[5],
            'Luck' : data[6],
            'Defense' : data[7],
            'Resistance' : data[8]
        }

    response = requests.get(BASE_URL[game] + 'characters/growth-rates/')
    content = response.content
    soup = BeautifulSoup(content, features='html.parser')
    characters = soup.find_all('tr')

    for character in characters:
        data = character.text.split('\n')

        if data[1].lower() == name.lower():
            return generate(data)

    return {'Character' : 'Not Found'}
