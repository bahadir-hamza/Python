'''
kenar = int(input("Karenin köşesini giriniz: "))

kareAlan = kenar**2
kareCevre = kenar*4

print("Karenin alanı:", kareAlan, "\nKarenin çevresi:", kareCevre)

'''
#########################
'''

unuzKnar = int(input("Dikkörtkenin uzun kenarını giriniz: "))
ksaKnar = int(input("Dittörkenin kısa kenarını giriniz: "))

alan = unuzKnar*ksaKnar
cevre = (unuzKnar+ksaKnar)*2

print("Dikdörtgenin alanı:", alan, "\nDikdörtgenin çevresi:", cevre)

'''
#########################

'''

cap = int(input("Dairenin yarıçapını giriniz: "))

daireAlan = 3*cap**2
daireCevre = 2*3*cap

print("Dairenin alanı:", daireAlan, "\nDairenin çevresi:", daireCevre)

'''

#########################

'''

adSoyad = input("Adınızı ve soyadınızı giriniz: ")

print("Hosgeldiniz Sn.", adSoyad)

'''

#########################

'''

enSevilen = input("En sevidiğin ders: ")

print("Belkide bijolojidst olmaloson")

'''

#########################

'''

m3 = int(input("Harcadığınız m3 miktarını giriniz: "))

m3Fiyat = 0.21
borc = m3*m3Fiyat

print("Bu ay ki faturanız:", borc)

'''

#########################

'''

yas = int(input("Kendi yaşınızı giriniz: "))
anne = int(input("Annenizin yaşını giriniz: "))
baba = int(input("Babanızın yaşını giriniz: "))
kardes = int(input("Kardeşinizin yaşını giriniz: "))
abi = int(input("Abinizin yaşlağını giriniz: "))
abla = int(input("Ablanızın yaşını giriniz: "))

ortalama = (yas+anne+baba+kardes+abi+abla)/6

print("Ailenizin yaş ortalaması:", ortalama)

'''

#########################

dogumYil = int(input("Doğum yılınızı giriniz: "))

yas = 2022-dogumYil

print(yas)