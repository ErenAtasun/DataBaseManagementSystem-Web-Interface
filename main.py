from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models

# Coded by ϽK
# github.com/mr-kartal
#linkedin.com/in/cagrikartal

"""
01001000 01100001 01111001 01100001
01110100 01110100 01100001 00100000
01100101 01101110 00100000 01101000
01100001 01101011 01101001 01101011
01101001 00100000 01101101 11000011
10111100 01110010 11000101 10011111
01101001 01110100 00100000 01101001
01101100 01101001 01101101 01100100
01101001 01110010 00100000 01100110
01100101 01101110 01100100 01101001
01110010
"""

app = FastAPI()

Base.metadata.create_all(bind=engine)


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/categories/", response_class=HTMLResponse)
def get_categories(request: Request, db: Session = Depends(get_db)):
    categories = db.query(models.Category).all()
    return templates.TemplateResponse("categories.html", {"request": request, "categories": categories})


@app.get("/customers/", response_class=HTMLResponse)
def get_customers(request: Request, db: Session = Depends(get_db)):
    customers = db.query(models.Customer).all()
    return templates.TemplateResponse("customers.html", {"request": request, "customers": customers})


@app.get("/products/", response_class=HTMLResponse)
def get_products(request: Request, db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return templates.TemplateResponse("products.html", {"request": request, "products": products})


@app.get("/payments/", response_class=HTMLResponse)
def get_payments(request: Request, db: Session = Depends(get_db)):
    payments = db.query(models.Payment).all()
    return templates.TemplateResponse("payments.html", {"request": request, "payments": payments})


@app.get("/orders/", response_class=HTMLResponse)
def get_orders(request: Request, db: Session = Depends(get_db)):
    orders = db.query(models.Orders).all()
    return templates.TemplateResponse("orders.html", {"request": request, "orders": orders})


@app.get("/deliveries/", response_class=HTMLResponse)
def get_deliveries(request: Request, db: Session = Depends(get_db)):
    deliveries = db.query(models.Delivery).all()
    return templates.TemplateResponse("deliveries.html", {"request": request, "deliveries": deliveries})


@app.get("/purchases/", response_class=HTMLResponse)
def get_purchases(request: Request, db: Session = Depends(get_db)):
    purchases = db.query(models.Purchase).all()
    return templates.TemplateResponse("purchases.html", {"request": request, "purchases": purchases})
