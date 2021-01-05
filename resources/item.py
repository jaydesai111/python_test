from flask import Flask, request
from flask_restful import Resource
from flask_jwt import JWT, jwt_required
import sqlite3
from models.item import ItemModel

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = ItemModel.item_by_name(name)
        if item:
            return item.json()
        
    def post(self, name):
        item = ItemModel.item_by_name(name)
        if item:
            return {'message':'item already exists'}

        data = request.get_json()
        item = ItemModel(name, **data)
       
        try:
           item.save_to_db()
        except:
            return {"message":"An error occoured while insert..."}, 500

        return item.json(), 201

    
    def delete(self,name):
        
        item = ItemModel.item_by_name(name)

        if item:
            item.delete_from_db()

        return {'message':'Iteam Deleted successfully...'}

class ItemList(Resource):

    def get(self):
        return {"Items": list(map(lambda x: x.json(),ItemModel.query.all()))}