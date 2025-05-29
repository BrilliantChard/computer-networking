class Farmer:
    def __init__(self, name, farm_size):
        self.name = name
        self.farm_size = farm_size

    def __str__(self):
        return f"Farmer {self.name} with a farm size of {self.farm_size} acres"

class Crop:
    def __init__(self, name, yield_per_acre):
        self.name = name
        self.yield_per_acre = yield_per_acre

    def __str__(self):
        return f"Crop {self.name} with a yield of {self.yield_per_acre} tons per acre"
    
class Farm:
    def __init__(self, farmer, crop):
        self.farmer = farmer
        self.crop = crop

    def calculate_yield(self):
        return self.farmer.farm_size * self.crop.yield_per_acre

    def __str__(self):
        return f"{self.farmer} growing {self.crop} with a total yield of {self.calculate_yield()} tons"