from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

class Category(Base):
    __tablename__ = "category"
    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String(100))
    category_type = Column(String(100))

class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    name = Column(String(100))
    surname = Column(String(100))
    password = Column(String(255))
    age = Column(Integer)
    adress = Column(Text)
    telephonenumber = Column(String(15))
    birthday = Column(Date)
    gender = Column(String(10))

class Delivery(Base):
    __tablename__ = "delivery"
    delivery_id = Column(Integer, primary_key=True, index=True)
    type = Column(String(100))
    status = Column(String(100))

class Product(Base):
    __tablename__ = "product"
    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(100))
    category_id = Column(Integer, ForeignKey("category.category_id"))
    color = Column(String(50))
    weight = Column(Numeric(10, 2))
    stock = Column(Integer)
    imageurl = Column(Text)

class Payment(Base):
    __tablename__ = "payment"
    payment_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    cvv = Column(Integer)
    exp_date = Column(Date)

class Orders(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    product_id = Column(Integer, ForeignKey("product.product_id"))
    delivery_id = Column(Integer, ForeignKey("delivery.delivery_id"))
    order_date = Column(Date)

class Purchase(Base):
    __tablename__ = "purchase"
    purchase_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    payment_id = Column(Integer, ForeignKey("payment.payment_id"))
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    adress = Column(Text)
    price = Column(Numeric(10, 2))
    e_invoice = Column(String(10))
