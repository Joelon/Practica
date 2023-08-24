from fastapi import Query, Path, APIRouter
from models.cancion import Cancion

router = APIRouter()

canciones = [
    {
        "id": 1,
        "name": "Remote Control",
        "artista": "Sussie 4 y Leon Larregui"
    },
    {
        "id": 2,
        "name": "Supremassive black hole",
        "artista": "MUSE"
    }
]

@router.get("/canciones")
def get_canciones():
    return canciones
#Nota
@router.get("/canciones/{id}")
def get_cancion(id: int = Path(gt=0)):
    return list(filter(lambda item: item['id'] == id, canciones))

@router.get("/canciones/")
def get_cancion(id: int, artista: str):
    return list(filter(lambda item: item['id'] == id and item['artista'] == artista, canciones))

@router.post("/canciones")
def create_cancion(cancion: Cancion):
    canciones.append(cancion)
    return canciones

@router.put("/canciones/{id}")
def update_cancion(id: int, cancion: Cancion):
    for index, item in enumerate(canciones):
        if item['id'] == id:
            canciones[index]['name'] = cancion.name
            canciones[index]['artista'] = cancion.artista
    return canciones

@router.delete("/canciones/{id}")
def delete_cancion(id: int):
    for item in canciones:
        if item['id'] == id:
            canciones.remove(item)
    return canciones
