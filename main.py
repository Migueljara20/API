from fastapi import FastAPI
from routes.producto_routes import router as produto_router
from routes.moneda_routes import router as moneda_router

app = FastAPI()

app.include_router(produto_router, prefix="/productos", tags=["produtos"])
app.include_router(moneda_router, prefix="/monedas", tags=["monedas"])

# Rutas de prueba
@app.get("/")
async def root():
    return {"message": "Hello World"}

