def promokod(xarid_summasi, minimal_xarid, chegirma_foizi, muddati_otgan):

    if muddati_otgan:
        print("Promokod muddati o'tgan")
        return

    if xarid_summasi < minimal_xarid:
        print("Minimal xarid summasiga yetmadi")
        return

    chegirma = xarid_summasi * chegirma_foizi / 100
    yakuniy_summa = xarid_summasi - chegirma

    print("Chegirma:", chegirma)
    print("Yakuniy summa:", yakuniy_summa)


xarid_summasi = int(input("Xarid summasi: "))
minimal_xarid = int(input("Minimal xarid summasi: "))
chegirma_foizi = float(input("Chegirma foizi: "))
muddati_otgan = input("Promokod muddati o'tganmi? (ha/yo'q): ")

if muddati_otgan == "ha":
    muddati_otgan = True
else:
    muddati_otgan = False

promokod(xarid_summasi, minimal_xarid, chegirma_foizi, muddati_otgan)