from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/RHBack_Assignment2"

mongo = PyMongo(app)

from app import routes