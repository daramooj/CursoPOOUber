from car import Car
from account import Account
from driver import Driver
from uberX import UberX
from user import User

if __name__ == "__main__":
    print("Hola mundo")
    # car = Car()
    # car.license = "AMK564"
    # car.driver = "Andres Herrera"
    # car.passegenger = 3
    # car.id = 1
    # print(vars(car))

    # car2 = Car()
    # car2.license = "NJN564"
    # car2.driver = "Andrea Herrera"
    # car2.passegenger = 5
    # car2.id = 2
    # print(vars(car2))

    car = Car("AMK564", Account("Andres Herrera","78998779G", "ejemplo@example.com", "4642151"), 4)
    print(vars(car))
    print(vars(car.driver))

    car2 = UberX("KJL486", Account("Luis Peralez","54345DSDF", "luis@ejemplo.com", "451215"), 4 , "T4000","Ford")
    print(vars(car2))
    print(vars(car2.driver))

    user = User("José José", "545155V", "Dos@platzi_ejemplo.com", "452556")
    print(vars(user))