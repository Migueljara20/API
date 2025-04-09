from fastapi import FastAPI
from routes.producto_routes import router as produto_router


app = FastAPI()

app.include_router(produto_router, prefix="/productos", tags=["produtos"])

# Rutas de prueba
@app.get("/")
async def root():
    return {"message": "Hello World"}

