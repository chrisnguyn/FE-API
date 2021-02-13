import FE6
import FE7
import FE8
import FE11


mapping = {
    'fe6' : FE6,
    'fe7' : FE7,
    'fe8' : FE8,
    'fe11' : FE11
}


def get_games() -> dict:
    return {
        'fe6' : 'Binding Blade',
        'fe7' : 'Blazing Blade',
        'fe8' : 'Sacred Stones',
        'fe11' : 'Awakening',
    }


def get_characters(game: str) -> dict:
    return mapping[game].get_characters.execute()


def get_growths(game: str, name: str) -> dict:
    return mapping[game].get_growths.execute(name)
