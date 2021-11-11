import uuid

class Product:
    def __init__(self, name, category, price):
        self.productId = str(uuid.uuid4())
        self.name = name
        self.category = category
        self.price = price
    
    def getPrice(self):
        return self.price
    
    def setPrice(self, price):
        self.price = price
        
    def getCategory(self):
        return self.category
    
    def setCategory(self, category):
        self.category = category
        
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
        
    def getProductId(self):
        return self.productId
    
    

class ProductFormatter:
    def format(self, product, formatAs):
        if formatAs == "text":
            return "Id: {},\nName: {},\nCategory: {},\nPrice: {}".format(product.getProductId(),product.getName(),product.getCategory(),product.getPrice())
        elif formatAs == "csv":
            return "{},{},{},{}".format(product.getProductId(),product.getName(),product.getCategory(),product.getPrice())
        return "Invalid Format"
    
    
def main():
    product = Product("Pepsi","Food", "50")
    formatter = ProductFormatter()
    print(formatter.format(product,"csv"))
    
if __name__ == "__main__":
    main()