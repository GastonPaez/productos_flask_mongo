from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://gpdevsl:<password>@cluster0.zd0ohox.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient.connect(MONGO_URI, tlsCAFile=ca)
        db = client["ddbb_products_app"]
    except ConnectionError:
        print("Error de conexion con la bbdd")
    return db


