from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://slgpdevsl:x8FQrIUdqTzW9QDc@cluster0.l68qbl0.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI,tlsCAFile=ca)
        db = client["ddbb_products_app"]
    except ConnectionError:
        print("Error de conexion con la bbdd")
    return db


