from fastapi import HTTPException
from db.producto_database import database_producto
from models.producto_model import ProductoBase


#Funcion que devuelve la lista de productos
def get_productos():
    print("📥 Endpoint /productos fue llamado")
    collection = database_producto.get_collection()
    productos = list(collection.find({}, {"_id": 0}))
    print("📦 Productos desde la base de datos:", productos)
    if not productos:        
        raise HTTPException(status_code=404, detail="No se encontraron productos, agrega algunos")
    return productos
    
#aqui se llama al producto por su id
def get_producto_id(producto_id: int):
    collection = database_producto.get_collection()
    producto = collection.find_one({"id": producto_id}, {"_id": 0})
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado, prueba con otro id") 
    return producto



#nuevo producto
def add_producto(producto: ProductoBase):
    collection = database_producto.get_collection()
    if collection.find_one({"id": producto.id}): 
        raise HTTPException(status_code=400, detail="El producto ya esta en la base de datos") #si el producto ya existe, se lanza una excepcion
    producto_dict = producto.dict()#Se convierte el producto a un diccionario

    collection.insert_one(producto_dict) #agrega un producto
    return{"Mensaje": "producto agregado a la base de datos"}



#aqui se actualiza el producto
def update_producto(producto_id: int, producto: ProductoBase):
    collection = database_producto.get_collection()
    producto_dict = producto.dict()
    if "id" in producto_dict:
        del producto_dict["id"] # evita que el id se actualice
    resultado = collection.update_one({"id": producto_id}, {"$set": producto_dict})
    if resultado.matched_count == 0: #Verifica si el producto existe
        raise HTTPException(status_code=404, detail="El producto no existe") #si no hay producto, se lanza una excepcion
    return{"Mensaje": "se actualizo el producto"}

#aqui se elimina un producto
def eliminar_producto(producto_id: int):
    collection = database_producto.get_collection()
    resultado = collection.delete_one({"id": producto_id})
    if resultado.deleted_count == 0: #Mira si el producto existe
        raise HTTPException(status_code=404, detail="El producto no existe") #si no existe, se lanza una excepcion
    return{"Mensaje": "Se elimino el producto"}