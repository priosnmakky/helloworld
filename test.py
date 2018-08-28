# Requires pymongo 3.6.0+
from flask import Flask
from pymongo import MongoClient
from flask_pymongo import PyMongo


# ###/client = MongoClient("mongodb://localhost:27017/")
# database = client["test"]
# collection = database["pompom"]
#
# # Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/
#
# app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
# mongo = PyMongo(app)
#
# query = {}
#
# cursor = collection.find(query)
# try:
#     for doc in cursor:
#         print(doc)
# finally:
#     client.close()




from flask import Flask, redirect, url_for, session, request, jsonify, abort
from flask_oauthlib.client import OAuth
