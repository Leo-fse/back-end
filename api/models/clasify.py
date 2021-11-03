from pydantic import BaseModel

class ClasifyData(BaseModel):
    model: str
    parts: str
    useKBN: str
    clasify: str
    NewProductKBN: str
    StockProductKBN: str
    relatedGcode: list

