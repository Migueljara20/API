from pydantic import BaseModel

#valida los datos con pydantic
class ProductoBase(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float
    stock: int