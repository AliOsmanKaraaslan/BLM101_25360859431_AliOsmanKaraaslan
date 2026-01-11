def rle_encode(metin):
    if not metin:
        return ""

    encoded = ""
    sayac = 1

    for i in range(1, len(metin)):
        if metin[i] == metin[i - 1]:
            sayac += 1
        else:
            encoded += str(sayac) + metin[i - 1]
            sayac = 1

    encoded += str(sayac) + metin[-1]
    return encoded


def rle_decode(s_metin):
    geri_acilmis = ""
    sayac = ""

    for i in s_metin:
        if i.isdigit():
            sayac += i
        else:
            geri_acilmis += i * int(sayac)
            sayac = ""

    return geri_acilmis


def oran(orijinal_metin, compressed):
    original_boyut = len(orijinal_metin)
    compressed_boyut = len(compressed)
    ratio = (1 - compressed_boyut / original_boyut) * 100
    return ratio


# ===== TEST =====
orijinal_metin = "AAAAABBBCCDAA"

s_metin = rle_encode(orijinal_metin)
acilmis_metin = rle_decode(s_metin)
ratio = oran(orijinal_metin, s_metin)


print("Orijinal Metin :", orijinal_metin)
print("Sıkıştırılmış  :", s_metin)
print("Geri Açılmış   :", acilmis_metin)
print("Sıkıştırma Oranı: %.2f%%" % ratio)
