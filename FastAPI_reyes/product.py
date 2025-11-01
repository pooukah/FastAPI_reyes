from sqlmodel import SQLModel, Field

# Model base
class product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    stock: int
    precio: float
    distribuidor: str       # informació sensible
    gastos: float           # informació sensible

    # precio seria el preu al que venem el producte
    # distribuidor seria el contacte d'on ho comprem
    # gastos seria els gastos total per a tindre el producte com a empresa

# Model per a crear productes (POST)
class createProduct(SQLModel):
    # no mostrem l'id ja que s'autoincrementa sol
    name: str
    stock: int
    precio: float
    distribuidor: str
    gastos: float

# Model per al públic (GET)
class productPublic(SQLModel):
    # Excluim els camps sensibles --> distribuidor i gastos
    id: int
    name: str
    stock: int
    precio: float