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

# Model amb tot pero no sensibles
class createProduct(SQLModel):
    # Treiem distribuidor y gastos
    id: int
    name: str
    stock: int
    precio: float

# Model per al públic (GET) (nomes 3 camps)
class productPublic(SQLModel):
    # Excluim els camps sensibles --> distribuidor i gastos
    name: str
    precio: float
    stock: int
