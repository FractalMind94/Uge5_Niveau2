import uuid
class Item:
    def __init__(self, band, price):
        self.band = band
        self.price = price
        self.id = uuid.uuid4()
        # self.name = name
        
    def __str__(self):
        return f"{self.band} (ID: {self.id}) - Price: ${self.price}"

class TShirt(Item):
    def __init__(self,  size, band):
        super().__init__("T-Shirt", 15)
        self.size = size

    def __str__(self):
        return f"{super().__str__()} - Size:{self.size} - Band: {self.band} - Price: {self.price}"
    
class Shorts(Item):
    def __init__(self, size, color, band):
        super().__init__("Shorts", 20)
        self.size = size
        self.color = color

    def __str__(self):
        return f"{super().__str__()} - Size: {self.size} - Band: {self.band} - Color: {self.color}"
class Hoodie(Item):
    def __init__(self,style, size, band):
        super().__init__("Hoodie", 30)
        self.size = size
        self.style = style

    def __str__(self):
        return f"{super().__str__()} - Size: {self.size} - Band: {self.band} - Style: {self.style}"
class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def connect(self):
        # Implement database connection here
        pass
class ItemFactory:
    @staticmethod
    def create_item(item_type, *args, **kwargs):
        if item_type == "T-Shirt":
            return TShirt(*args, **kwargs)
        elif item_type == "Shorts":
            return Shorts(*args, **kwargs)
        elif item_type == "Hoodie":
            return Hoodie(*args, **kwargs)
        # Add more item types as needed
        else:
            raise ValueError("Invalid item type")
def main():
    db_connection = DatabaseConnection()
    tshirt = ItemFactory.create_item("T-Shirt", size= "L", band= "Obscura")
    shorts = ItemFactory.create_item("Shorts", size="L", color="Black", band= "Obscura")
    hoodie = ItemFactory.create_item("Hoodie", size="L", style="Long-Sleeve", band= "Obscura")
    print(tshirt)
    print(shorts)
    print(hoodie)
    

if __name__ == "__main__":
    main()



        
