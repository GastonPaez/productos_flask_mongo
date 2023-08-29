class Product():
    def __init__(self, name,price,quantity):
        self.name = name 
        self.price = price 
        self.quantity = quantity 

    # Devuelve objeto con los atributos para guardar en la collection de la DB
    def toDBCollection(self):
        return{
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }
    
