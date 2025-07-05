
from flask import Flask,request

app = Flask(__name__)

stores = [
    {
        "name" : "My Store",
        "items": [
            {
                "name":"Sandeep",
                "id" : 12345
            }
        ]
    }
]

@app.get("/store")
def get_stores():
    print("in get_stores")
    return {"stores":stores}


@app.post("/store")
def create_store():
    print("in create_store")
    rx_request = request.get_json()
    new_store = {"name":rx_request["name"]+"1","items":[]}
    stores.append(new_store)
    rx_request = request.get_json()
    new_store = {"name":rx_request["name"]+"2","items":[]}
    stores.append(new_store)
    return new_store,201

@app.post("/store/<string:name>/item")
def create_item(name):
    print("in create_item")
    rx_request = request.get_json()
    print(rx_request)
    for store in stores:
        print(store["name"])
        if store["name"] == name:
            new_item = {"name":rx_request["name"],"id":rx_request["id"]}
            store["items"].append(new_item)
            return new_item,201
    return {"message":"No Store found"} ,404

@app.post("/store/<string:name>/")
def getStore(name):
    print("in getStore")
    for store in stores:
        if store["name"] == name:
            return store,201
    return {"message":"No Store found"} ,404