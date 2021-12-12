from car import Car


class UberX(Car):
    model: str
    brand: str

    def __init__(self, license, driver, passegenger, model, brand):
        super().__init__(license, driver, passegenger)
        self.model = model 
        self.brand = brand
