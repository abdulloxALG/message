class ParkingLot:
    def __init__(self, joy, narx):
        self.joy = joy
        self.narx = narx
        self.mashinalar = []

    def park_car(self, raqam):
        if len(self.mashinalar) < self.joy:
            self.mashinalar.append(raqam)
            print(raqam, "park qilindi")
        else:
            print("Bosh joy yoq")

    def unpark_car(self, raqam):
        if raqam in self.mashinalar:
            soat = int(input("Necha soat turdi? "))
            tolov = soat * self.narx

            self.mashinalar.remove(raqam)

            print("Mashina chiqarildi")
            print("Tolov:", tolov, "som")
        else:
            print("Mashina topilmadi")


parking = ParkingLot(3, 5000)

raqam = input("Mashina raqami: ")
parking.park_car(raqam)

raqam = input("Chiqadigan mashina raqami: ")

parking.unpark_car(raqam)