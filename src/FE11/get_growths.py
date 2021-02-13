import requests
from bs4 import BeautifulSoup


def execute(name):
    def generate(data):
        return {
            'Character' : data[1],
            'Health' : data[2],
            'Strength' : data[3],
            'Magic' : data[4],
            'Skill' : data[5],
            'Speed' : data[6],
            'Luck' : data[7],
            'Defense' : data[8],
            'Resistance' : data[9]
        }

    response = requests.get('https://serenesforest.net/awakening/characters/growth-rates/base/')
    content = response.content
    soup = BeautifulSoup(content, features='html.parser')
    characters = soup.find_all('tr')

    for character in characters:
        data = character.text.split('\n')

        if data[1].lower() == name.lower():
            return generate(data)

    return {'Character' : 'Not Found'}
