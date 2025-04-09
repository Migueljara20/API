from fastapi import APIRouter
from models.producto_model import ProductoBase
from services.producto_service import get_productos, get_producto_id, add_producto, update_producto, eliminar_producto
from db.producto_database import database_producto

router = APIRouter()

#ruta de pureba agrega un producto a la base de datos
@router.post("/test")
def crear_producto_test():
    collection = database_producto.get_collection()
    producto_nuevo = {
        "nombre": "Producto de prueba",
        "precio": 9.99,
        "stock": 5
    }
    result = collection.insert_one(producto_nuevo)
    return {"mensaje": "Producto insertado", "id": str(result.inserted_id)}


#lista general de peliculas
@router.get("/lista", response_model=list[ProductoBase])
async def get_productos_list():
    productos = get_productos()
    return productos



#producto por id
@router.get("/{producto_id}", response_model=ProductoBase)
async def get_pelicula(producto_id: int):
    producto = get_producto_id(producto_id)
    if producto:
        return producto
    

#agrega un nuevo producto a la base de datos
@router.post("/agregar", response_model=dict)
async def create_pelicula(producto: ProductoBase):
    return add_producto(producto)

#actualiza los datos de un producto en la base de datos
@router.put("/actualizar/{producto_id}", response_model=dict)
async def actualizar_producto(producto_id: int, producto: ProductoBase):
    return update_producto(producto_id, producto)

#Elimina un producto de la base de datos
@router.delete("/eliminar/{producto_id}", response_model=dict)
async def delete_producto(producto_id: int):
    return eliminar_producto(producto_id)