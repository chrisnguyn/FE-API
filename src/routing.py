import FE6
import FE7
import FE8


mapping = {
    'fe6' : FE6,
    'fe7' : FE7,
    'fe8' : FE8
}


def get_characters(game: str) -> dict:
    return mapping[game].get_characters.execute()


def get_growths(game: str, name: str) -> dict:
    return mapping[game].get_growths.execute(name)
