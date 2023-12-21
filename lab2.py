from fastapi import *
from pydantic import BaseModel
from wikipedia import *


app = FastAPI(
    title='Поисковик'
)


class GeoInput(BaseModel):
    x: float
    y: float


class GeoOutput(BaseModel):
    info: str

@app.get('/path_search/{word}')
def path(word: str):
    try:
        return {wikipedia.page(word).content}
    except PageError:
        raise HTTPException(status_code=404)


@app.get('/query_search')
def query(word: str):
    try:
        return {'result': wikipedia.page(word).categories}
    except PageError:
        raise HTTPException(status_code=404)


@app.post('/body_geosearch')
def postByBody(coord: GeoInput):
    try:
        return GeoOutput(info=str(wikipedia.geosearch(coord.x, coord.y)))
    except PageError:
        raise HTTPException(status_code=404)