def ecommerce(xarid_summasi, promokod, muddati_otgan, chegirma_foizi):

    if promokod != "SALE20":
        print("Promokod noto'g'ri.")
        print("To'lanadigan summa:", xarid_summasi, "so'm")

    elif muddati_otgan:
        print("Promokod muddati o'tgan.")
        print("To'lanadigan summa:", xarid_summasi, "so'm")

    else:
        chegirma = xarid_summasi * chegirma_foizi / 100
        yakuniy_summa = xarid_summasi - chegirma

        print("Promokod qabul qilindi!")
        print("Xarid summasi:", xarid_summasi, "so'm")
        print("Chegirma:", chegirma, "so'm")
        print("To'lanadigan summa:", yakuniy_summa, "so'm")


xarid_summasi = float(input("Xarid summasi: "))

promokod = input("Promokod kiriting: ")

muddati = input("Promokod muddati o'tganmi? (ha/yo'q): ").lower()

if muddati == "ha":
    muddati_otgan = True
else:
    muddati_otgan = False

chegirma_foizi = float(input("Chegirma foizi: "))


ecommerce(xarid_summasi, promokod, muddati_otgan, chegirma_foizi)