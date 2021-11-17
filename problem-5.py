import uuid

class Product:
    def __init__(self, name, category, price):
        self.product_id = str(uuid.uuid4())
        self.name = name
        self.category = category
        self.price = price
    
    @property
    def price(self):
        return self.price
    
    @price.setter
    def price(self, price):
        self.price = price
        
    @property
    def category(self):
        return self.category
    
    @category.setter
    def category(self, category):
        self.category = category
        
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, name):
        self.name = name
        
    @property
    def product_id(self):
        return self.product_id
    
    

class ProductFormatter:
    def format(self, product, format_as):
        if format_as == "text":
            return "Id: {},\nName: {},\nCategory: {},\nPrice: {}".format(product.product_id,product.name,product.category,product.price)
        elif format_as == "csv":
            return "{},{},{},{}".format(product.product_id,product.name,product.category,product.price)
        return "Invalid Format"
    

    
if __name__ == "__main__":
    product = Product("Pepsi","Food", "50")
    formatter = ProductFormatter()
    print(formatter.format(product,"csv"))
    