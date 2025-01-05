from pydantic import BaseModel
from datetime import date
from typing import Optional

class CategoryBase(BaseModel):
    category_name: str
    category_type: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    category_id: int
    class Config:
        from_attributes = True


class CustomerBase(BaseModel):
    email: str
    name: str
    surname: str
    age: int
    adress: str
    telephonenumber: str
    birthday: date
    gender: str

class CustomerCreate(CustomerBase):
    password: str

class CustomerResponse(CustomerBase):
    customer_id: int
    class Config:
        from_attributes = True


class DeliveryBase(BaseModel):
    type: str
    status: str

class DeliveryCreate(DeliveryBase):
    pass

class DeliveryResponse(DeliveryBase):
    delivery_id: int
    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    product_name: str
    category_id: int
    color: str
    weight: float
    stock: int
    imageurl: str

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    product_id: int
    class Config:
        from_attributes = True


class PaymentBase(BaseModel):
    customer_id: int
    cvv: int
    exp_date: date

class PaymentCreate(PaymentBase):
    pass

class PaymentResponse(PaymentBase):
    payment_id: int
    class Config:
        from_attributes = True


class OrdersBase(BaseModel):
    customer_id: int
    product_id: int
    delivery_id: int
    order_date: date

class OrdersCreate(OrdersBase):
    pass

class OrdersResponse(OrdersBase):
    order_id: int
    class Config:
        from_attributes = True


class PurchaseBase(BaseModel):
    customer_id: int
    payment_id: int
    order_id: int
    adress: str
    price: float
    e_invoice: str

class PurchaseCreate(PurchaseBase):
    pass

class PurchaseResponse(PurchaseBase):
    purchase_id: int
    class Config:
        from_attributes = True
