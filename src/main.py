from auxiliary import *
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()


@app.get('/')
def main():
    return 'FE API - The Unofficial Fire Emblem API :)'


@app.get('/error')
def error():
    return 'Nothing to see here :('


@app.get('/{game}/characters')  # character list + recruitment
def read_characters(game: str):
    return get_characters(game)


@app.get('/{game}/growths/{character}')  # growths
def read_stats(game: str, character: str):
    return get_stats(game, character)


@app.exception_handler(StarletteHTTPException)
def custom_http_exception_handler(request, exc):
    return RedirectResponse('/error')