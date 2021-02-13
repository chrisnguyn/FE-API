import requests
from bs4 import BeautifulSoup


def execute(name):
    def generate(data):
        supports = []

        for cell in data[2:]:
            if cell and cell[0].isalpha():
                supports.append(cell.split(' ')[0])

        return supports

    response = requests.get('https://serenesforest.net/the-sacred-stones/characters/supports/')
    content = response.content
    soup = BeautifulSoup(content, features='html.parser')
    characters = soup.find_all('tr')

    for character in characters:
        data = character.text.split('\n')
        if data[1].strip().lower() == name.lower():
            return generate(data)

    return {'Character' : 'Not Found'}
