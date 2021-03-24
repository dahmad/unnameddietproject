import os
import boto3
from flask import Flask, jsonify, request


app = Flask(__name__)

IS_OFFLINE = os.environ.get('IS_OFFLINE')

# Database Tables
RECIPES_TABLE = os.environ['RECIPES_TABLE']
INGREDIENTS_TABLE = os.environ['INGREDIENTS_TABLE']
STORES_TABLE = os.environ['STORES_TABLE']
INVENTORY_CHECKLISTS_TABLE = os.environ['INVENTORY_CHECKLISTS_TABLE']
SHOPPING_LISTS_TABLE = os.environ['SHOPPING_LISTS_TABLE']
COOKING_WORKFLOWS_TABLE = os.environ['COOKING_WORKFLOWS_TABLE']
CALENDARS_TABLE = os.environ['CALENDARS_TABLE']

if IS_OFFLINE:
    client = boto3.client(
        'dynamodb',
        region_name='localhost',
        endpoint_url='http://localhost:8000'
    )
else:
    client = boto3.client('dynamodb')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/v1/recipes/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def recipes():
    return

@app.route("/api/v1/ingredients/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def ingredients():
    return

@app.route("/api/v1/stores/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def stores():
    return

@app.route("/api/v1/inventory_checklists/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def inventory_checklists():
    return

@app.route("/api/v1/shopping_lists/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def shopping_lists():
    return

@app.route("/api/v1/cooking_workflows/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def cooking_workflows():
    return

@app.route("/api/v1/calendars/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def calendars():
    return