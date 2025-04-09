from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class DatabaseProducto:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGO_URI"), tlsAllowInvalidCertificates=True) #Aca se hace la conexion con la base de datos
        self.db = self.client[os.getenv("MONGO_DB_NAME")] #Aca se selecciona la coleccion de la base de datos

    def get_collection(self):        
        return self.db[os.getenv("COLLECTION_PRODUCTO")] #Aca se selecciona la coleccion de la base de datos

database_producto = DatabaseProducto() #Aca se instancia la clase DatabaseProducto