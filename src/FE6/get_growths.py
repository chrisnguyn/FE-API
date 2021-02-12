import requests
from bs4 import BeautifulSoup


def execute(name):
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

    response = requests.get('https://serenesforest.net/binding-blade/characters/growth-rates/')
    content = response.content
    soup = BeautifulSoup(content, features='html.parser')
    characters = soup.find_all('tr')

    for character in characters:
        data = character.text.split('\n')

        if data[1].lower() == name.lower():
            return generate(data)

    return {'Character' : 'Not Found'}
