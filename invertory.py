class Guitar: 
    def __init__(self, serial_number, price, builder, model, guitar_type):
        self.serial_number = serial_number
        self.price = price
        self.builder = builder
        self.model = model
        self.guitar_type = guitar_type
        
class Customer: 
    def __init__(self, name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self, guitar):
        self.cart.append(guitar)
        
    def calculate_total(self):
        total = sum(guitar.price for guitar in self.cat)
        if len(self.cart) > 1:
            total *= 0.95 
        total_width_taxes = total * 1.15 
        
        return total_width_taxes
    

class InventoryManagement:
    def __init__(self):
        self.inverntory = [ ]
    
    def add_guitar(self, guitar):
        self.inverntory.append(guitar)
        
    def search(self, keyword):
        results = []
        for guitar in self.inverntory:
            if(
                keyword in guitar.serial_number
                or keyword in guitar.builder
                or keyword in guitar.model
                or keyword in guitar.guitar_type
            ):
                results.append(guitar)
            return results
        
#unit test     
        
def test_inverntory_management():
    inverntory_system =InventoryManagement()
    
    guitar1 = Guitar("")
    guitar2 = Guitar("")
    inverntory_system.add_guitar(guitar1)
    inverntory_system.add_guitar(guitar2)
    
    assert len(inverntory_system.inverntory) == 2
    
    results = inverntory_system.search("les paul")
    assert len(results) == 1
    assert results[0].builder == ""
    
    customer = Customer("")
    customer.add_to_cart(guitar1)
    customer.add_to_cart(guitar2)
    total = customer.calculate_total()
    
    assert total == 3282.5 # 
    
if __name__ == "__main__":
    test_inverntory_management()
    print("All ")
    
                
        