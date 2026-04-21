from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import Dish

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SGF - Gestión de Restaurante")

@app.get("/")
def home():
    return {"mensaje": "Conectado a MySQL y funcionando"}

@app.get("/menu")
def get_menu(db: Session = Depends(get_db)):
    dishes = db.query(Dish).all()
    return dishes
@app.post("/menu")
def create_dish(name: str, price: float, description: str = None, db: Session = Depends(get_db)):
    nuevo_plato = Dish(name=name, price=price, description=description)
    db.add(nuevo_plato)
    db.commit()
    db.refresh(nuevo_plato)
    return {"mensaje": "Platillo guardado", "dato": nuevo_plato}