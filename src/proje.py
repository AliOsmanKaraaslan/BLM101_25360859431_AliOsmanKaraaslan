# Run-Length Encoding (RLE) ile sıkıştırma fonksiyonu
def rle_encode(metin):
    # Eğer metin boşsa boş string döndür
    if not metin:
        return ""

    encoded = ""   # Sıkıştırılmış metni tutacak değişken
    sayac = 1      # Ardışık karakter sayacı

    # Metnin 2. karakterinden başlayarak döngü
    for i in range(1, len(metin)):
        # Eğer mevcut karakter öncekiyle aynıysa sayaç artırılır
        if metin[i] == metin[i - 1]:
            sayac += 1
        else:
            # Farklı karakter gelirse, sayaç ve karakter eklenir
            encoded += str(sayac) + metin[i - 1]
            sayac = 1  # Sayaç sıfırlanır

    # Döngü bittikten sonra son karakter grubu eklenir
    encoded += str(sayac) + metin[-1]
    return encoded


# RLE ile sıkıştırılmış metni geri açma (decode) fonksiyonu
def rle_decode(s_metin):
    geri_acilmis = ""  # Açılmış metni tutar
    sayac = ""        # Sayıyı string olarak toplamak için

    # Sıkıştırılmış metindeki her karakter için
    for i in s_metin:
        # Eğer karakter rakamsa sayaca ekle
        if i.isdigit():
            sayac += i
        else:
            # Harf geldiğinde, harfi sayaç kadar çoğalt
            geri_acilmis += i * int(sayac)
            sayac = ""  # Sayaç sıfırlanır

    return geri_acilmis


# Sıkıştırma oranını hesaplayan fonksiyon
def oran(orijinal_metin, compressed):
    original_boyut = len(orijinal_metin)   # Orijinal metnin uzunluğu
    compressed_boyut = len(compressed)     # Sıkıştırılmış metnin uzunluğu

    # Sıkıştırma yüzdesi hesaplama
    ratio = (1 - compressed_boyut / original_boyut) * 100
    return ratio


# ===== TEST KISMI =====
orijinal_metin = "AAAAAAAAABBBBBBBBBBBCCDAA"

# Metni sıkıştır
s_metin = rle_encode(orijinal_metin)

# Sıkıştırılmış metni geri aç
acilmis_metin = rle_decode(s_metin)

# Sıkıştırma oranını hesapla
ratio = oran(orijinal_metin, s_metin)

# Sonuçları ekrana yazdır
print("Orijinal Metin :", orijinal_metin)
print("Sıkıştırılmış  :", s_metin)
print("Geri Açılmış   :", acilmis_metin)
print("Sıkıştırma Oranı: %.2f%%" % ratio)
