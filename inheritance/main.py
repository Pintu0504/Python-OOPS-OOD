import csv

class Item:
    pay_rate = 0.8 # Price after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Validate attributes 
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"

        # Assign attributes to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to take
        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                item.get('name'),
                float(item.get('price')),
                int(item.get('quantity'))
            )
    
    @staticmethod
    def is_integer(num):
        # We want to count out from float for point zero numbers
        # Eg- 5.0 and 7.0 should be considered int
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.price}, {self.quantity})"


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity
        )

        # Validate attributes 
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to zero"
    
        # Assign attributes to self object
        self.broken_phones = broken_phones


phone1 = Phone("Poco f1", 100, 2, 1)
print(Item.all)