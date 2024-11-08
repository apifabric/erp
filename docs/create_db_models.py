# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()

class Customer(Base):
    """
    description: Stores customer details including contact information and credit data.
    """
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    credit_limit = Column(Float, nullable=True)
    balance = Column(Float, nullable=True, default=0.0)

class Product(Base):
    """
    description: Contains product information including name, description, and price.
    """
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)

class Order(Base):
    """
    description: Represents customer orders including total amount and shipment details.
    """
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    date_ordered = Column(DateTime, default=datetime.now, nullable=False)
    date_shipped = Column(DateTime, nullable=True)
    amount_total = Column(Float, nullable=True, default=0.0)

class OrderItem(Base):
    """
    description: Links products to orders with quantity and calculated item amount.
    """
    __tablename__ = 'order_items'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    unit_price = Column(Float, nullable=False)
    amount = Column(Float, nullable=True, default=0.0)

class Supplier(Base):
    """
    description: Holds supplier information including contact details.
    """
    __tablename__ = 'suppliers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=True)

class Inventory(Base):
    """
    description: Keeps track of product inventory levels per warehouse.
    """
    __tablename__ = 'inventory'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

class Warehouse(Base):
    """
    description: Stores information about different warehouses.
    """
    __tablename__ = 'warehouses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    location = Column(String, nullable=False)
    capacity = Column(Integer, nullable=True)

class Shipment(Base):
    """
    description: Contains shipment details for orders including warehouse handling.
    """
    __tablename__ = 'shipments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    warehouse_id = Column(Integer, ForeignKey('warehouses.id'), nullable=False)
    date_shipped = Column(DateTime, nullable=True)

class Payment(Base):
    """
    description: Details of payments made by customers for their orders.
    """
    __tablename__ = 'payments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    amount = Column(Float, nullable=False)
    date_paid = Column(DateTime, nullable=False, default=datetime.now)

class SupplierProduct(Base):
    """
    description: Junction table mapping suppliers to products they supply.
    """
    __tablename__ = 'supplier_products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)

class Category(Base):
    """
    description: Describes categories for products including name and description.
    """
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)

class ProductCategory(Base):
    """
    description: Junction table for linking products to categories.
    """
    __tablename__ = 'product_categories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

# Create an engine and a session
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Adding sample data
customers = [
    Customer(name="Alice Smith", email="alice@example.com", phone="1234567890", credit_limit=5000.0, balance=300.0),
    Customer(name="Bob Johnson", email="bob@example.com", phone="0987654321", credit_limit=3000.0, balance=150.0),
]

products = [
    Product(name="Laptop", description="A high performance laptop", price=1200.00),
    Product(name="Mouse", description="Wireless optical mouse", price=25.00),
]

orders = [
    Order(customer_id=1, date_ordered=datetime.now(), amount_total=1250.0),
    Order(customer_id=2, date_ordered=datetime.now(), date_shipped=datetime.now(), amount_total=50.0),
]

order_items = [
    OrderItem(order_id=1, product_id=1, quantity=1, unit_price=1200.00, amount=1200.00),
    OrderItem(order_id=2, product_id=2, quantity=2, unit_price=25.00, amount=50.00),
]

suppliers = [
    Supplier(name="Supplier A", phone="3216549870"),
    Supplier(name="Supplier B", phone="9876543210"),
]

inventory = [
    Inventory(product_id=1, quantity=50),
    Inventory(product_id=2, quantity=200),
]

warehouses = [
    Warehouse(location="New York", capacity=1000),
    Warehouse(location="Los Angeles", capacity=500),
]

shipments = [
    Shipment(order_id=1, warehouse_id=1, date_shipped=datetime.now()),
    Shipment(order_id=2, warehouse_id=2, date_shipped=datetime.now()),
]

payments = [
    Payment(order_id=1, amount=1250.0, date_paid=datetime.now()),
    Payment(order_id=2, amount=50.0, date_paid=datetime.now()),
]

supplier_products = [
    SupplierProduct(supplier_id=1, product_id=1),
    SupplierProduct(supplier_id=2, product_id=2),
]

categories = [
    Category(name="Electronics", description="Electronic devices and accessories"),
    Category(name="Accessories", description="Consumer electronics accessories"),
]

product_categories = [
    ProductCategory(product_id=1, category_id=1),
    ProductCategory(product_id=2, category_id=2),
]

session.add_all(customers)
session.add_all(products)
session.add_all(orders)
session.add_all(order_items)
session.add_all(suppliers)
session.add_all(inventory)
session.add_all(warehouses)
session.add_all(shipments)
session.add_all(payments)
session.add_all(supplier_products)
session.add_all(categories)
session.add_all(product_categories)
session.commit()
session.close()
