# Soru 1
harfler = ["a", "e", "i", "o", "i", "u"]
print(harfler.count("i"), "tane i harfi var.", harfler.count("p"), "tane p harfi var.")

# Soru 2
liste1, liste2, liste3, liste4 = ["a"], ["b"], ["c"], ["d"]
print(liste1, liste2, liste3, liste4)

# Soru 3
liste1 = ["bu", "bir"]
liste2 = ["yazı"]
liste3 = []
liste3.append(liste1 + liste2)
print(liste3)

# Soru 4
liste = [34, 1, 56, 334, 23, 2, 3, 19]
liste.sort()
print(liste)
liste.reverse()
print(liste)

# Soru 5
listem = ["Merhaba", "Türkiye", "Nasılsın", "Tebrikler"]
print(listem[-1])
print(listem[-3])
print(listem[-4])

# Soru 6
liste = [1, 2, 3, 4, 5, 6, 7]
print(liste[1:3])
print(liste[0:3])
print(liste[3::])
print(liste[::])

# Soru 7
isimler = ["ali", "veli", "ayşe"]
soyisimler = ["türk", "izci", "erel"]
ad_soy1 = isimler[0] + ' ' + soyisimler[0]
ad_soy2 = isimler[1] + ' ' + soyisimler[1]
ad_soy3 = isimler[2] + ' ' + soyisimler[2]
print(ad_soy1)
print(ad_soy2)
print(ad_soy3)

# Soru 8
liste = ["bir", "iki", "dört"]
print(liste)
liste.insert(2, "üç")
liste.append("beş")
print(liste)

# Soru 9

liste = ["birinci veri", "ikinci veri", "üçüncü veri", "dördüncü veri", "beşinci veri"]
print(liste[0])
print(liste[4])