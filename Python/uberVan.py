from car import Car

class uberVan(Car):
    seatsMaterial = []
    typeCardAccepted = []

    def __init__(self, license, driver, seatsMaterial, typeCardAccepted):
        super.__init__(license, driver)
        self.seatsMaterial = seatsMaterial
        self.typeCardAccepted = typeCardAccepted
        