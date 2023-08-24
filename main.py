from fastapi import FastAPI
from routers.cancion import router as song_router
import httpx

app = FastAPI()

@app.get("/")
def index():
    return {"message" : "Bienvenidos al reventón musical, elije las canciones que quieras escuchar."}

app.include_router(song_router)

@app.get("/consumir-api-externa")
async def consumir_api_externa():
    url = "https://pokeapi.co/api/v2/pokemon/ditto"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()
