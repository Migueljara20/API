from fastapi import APIRouter, Query, HTTPException
from services.moneda_service import convertir_moneda

router = APIRouter()

@router.get("/convertir")
def convertir(
    from_currency: str = Query(..., alias="de"),
    to_currency: str = Query(..., alias="a"),
    amount: float = Query(..., alias="monto")
):
    try:
        resultado = convertir_moneda(from_currency.upper(), to_currency.upper(), amount)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
