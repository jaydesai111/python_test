from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.secret_key = 'jay'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
api = Api(app)
jwt = JWT(app, authenticate, identity)
items=[]

@app.before_first_request
def create_table():
    db.create_all()

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList,'/itemlist')
api.add_resource(Store,'/stores/<string:name>')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register')

if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5002,debug=True)
