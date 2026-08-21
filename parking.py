class ParkingLot:

    def __init__(self, joy):
        self.joy = joy
        self.mashinalar = []

    # 1. Mashina qo'shish
    def mashina_qoshish(self, raqam):

        if len(self.mashinalar) >= self.joy:
            print("\nParking to'la!")
            return

        if raqam in self.mashinalar:
            print("\nBu mashina allaqachon parkingda!")
            return

        self.mashinalar.append(raqam)

        print("\n", raqam, "parkingga qo'shildi.")


    # 2. Mashina chiqarish
    def mashina_chiqarish(self, raqam):

        if raqam in self.mashinalar:

            self.mashinalar.remove(raqam)

            print("\n", raqam, "parkingdan chiqarildi.")

        else:

            print("\nBunday mashina parkingda yo'q.")


    # 3. Parkingdagi barcha mashinalarni ko'rsatish
    def mashinalarni_korsatish(self):

        print("\n==============================")
        print("       PARKING HOLATI")
        print("==============================")

        # Parkingdagi mashinalar
        if len(self.mashinalar) == 0:

            print("Parking bo'sh.")

        else:

            print("Parkingdagi mashinalar:")

            for raqam in self.mashinalar:
                print("-", raqam)

        # Joylar haqida ma'lumot
        band = len(self.mashinalar)
        bosh = self.joy - band

        print("\nJami joy:", self.joy)
        print("Band joy:", band)
        print("Bo'sh joy:", bosh)


# ==========================================
# PARKING YARATISH
# ==========================================

parking = ParkingLot(5)


# ==========================================
# ASOSIY MENYU
# ==========================================

while True:

    print("\n==============================")
    print("         PARKING LOT")
    print("==============================")

    print("1. Mashina qo'shish")
    print("2. Mashina chiqarish")
    print("3. Parkingdagi hamma mashinalar")
    print("4. Chiqish")

    tanlov = input("\nTanlang: ")


    # ======================================
    # 1. MASHINA QO'SHISH
    # ======================================

    if tanlov == "1":

        raqam = input(
            "Mashina raqamini kiriting: "
        ).upper()

        parking.mashina_qoshish(raqam)


    # ======================================
    # 2. MASHINA CHIQARISH
    # ======================================

    elif tanlov == "2":

        raqam = input(
            "Chiqadigan mashina raqamini kiriting: "
        ).upper()

        parking.mashina_chiqarish(raqam)


    # ======================================
    # 3. BARCHA MASHINALAR
    # ======================================

    elif tanlov == "3":

        parking.mashinalarni_korsatish()


    # ======================================
    # 4. DASTURDAN CHIQISH
    # ======================================

    elif tanlov == "4":

        print("\nDastur tugadi. Xayr!")

        break


    # ======================================
    # NOTO'G'RI TANLOV
    # ======================================

    else:

        print("\nNoto'g'ri tanlov! 1-4 orasidagi raqamni tanlang.")
