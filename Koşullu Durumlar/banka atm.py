print("""*************************
Atm Makinesine Hoşgeldiniz.

İşlemler;

1.Bakiye Sorgulama

2.Para yatırma

3.Para çekme

Programdan çıkmak için 'q'ya basın.
**********************************
""")
bakiye = 500
while True:
    islem = input("yapmak istediğiniz işlemi seçiniz:")
    if (islem == 'q'):
        print("tekrar bekleriz")
        break
    elif (islem == "1"):
        print("{} tl'dir.".format(bakiye))
    elif (islem == "2"):
        miktar = int(input("yatırılacak para:"))
        bakiye += miktar
        print("{} yeni bakiyeniz".format(bakiye))
    elif(islem == "3"):
        miktar = int(input("çekmek istediğiniz tutar: "))
        if (bakiye - miktar < 0):
         print("bu işlemi yapamazsınız")
         continue
        bakiye -= miktar

    else:
     print("gecersiz islem...")