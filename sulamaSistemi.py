
class Device:
    def __init__(self, name):
        self.name = name
        self.aktif = False

    def ac(self):
        self.aktif = True
        print(f"{self.name} açıldı.")

    def kapa(self):
        self.aktif = False
        print(f"{self.name} kapatıldı.")

    def durum_goster(self):
        durum = "Açık" if self.aktif else "Kapalı"
        print(f"{self.name} durumu: {durum}")


class SicaklikSensoru(Device):
    def __init__(self, name, sicaklik):
        super().__init__(name)
        self.__sicaklik = sicaklik

    def sicaklik_oku(self):
        return self.__sicaklik

    def sicaklik_guncelle(self, yeni_sicaklik):
        self.__sicaklik = yeni_sicaklik

    def bilgi_goster(self):
        print(f"{self.name}: {self.__sicaklik} °C")


class NemSensoru(Device):
    def __init__(self, name, nem):
        super().__init__(name)
        self.__nem = nem

    def nem_oku(self):
        return self.__nem

    def nem_guncelle(self, yeni_nem):
        if 0 <= yeni_nem <= 100:
            self.__nem = yeni_nem
        else:
            print("Nem değeri 0-100 arasında olmalıdır.")

    def bilgi_goster(self):
        print(f"{self.name}: %{self.__nem}")


class SulamaSistemi(Device):
    def __init__(self, name, ayar):
        super().__init__(name)
        self.__ayar = 5

        self.ayarla(ayar)

    def ayarla(self, ayar):
        if 1 <= ayar <= 10:
            self.__ayar = ayar
            print(f"Su akış hızı {ayar} olarak ayarlandı.")
        else:
            print("Geçersiz ayar! 1-10 arasında değer giriniz.")

    def sulama_yap(self):
        if self.aktif:
            print(
                f"{self.name} çalışıyor. "
                f"Su akış hızı: {self.__ayar}"
            )
        else:
            print("Sulama sistemi kapalı! Önce sistemi açmalısınız.")

    def bilgi_goster(self):
        print(f"{self.name} - Su akış ayarı: {self.__ayar}")


class SulamaKontrol:
    def __init__(self, sicaklik_sensoru, nem_sensoru, sulama_sistemi):
        self.sicaklik_sensoru = sicaklik_sensoru
        self.nem_sensoru = nem_sensoru
        self.sulama_sistemi = sulama_sistemi

    def otomatik_kontrol(self):
        nem = self.nem_sensoru.nem_oku()
        sicaklik = self.sicaklik_sensoru.sicaklik_oku()

        print("\n--- Otomatik Kontrol ---")
        print(f"Anlık sıcaklık: {sicaklik} °C")
        print(f"Anlık nem: %{nem}")

        if nem < 30 and sicaklik > 25:
            print("Toprak nemi düşük ve sıcaklık yüksek.")
            print("Sulama başlatılıyor...")

            self.sulama_sistemi.ac()
            self.sulama_sistemi.sulama_yap()

        elif nem < 30:
            print("Toprak nemi düşük.")
            print("Sulama başlatılıyor...")

            self.sulama_sistemi.ac()
            self.sulama_sistemi.sulama_yap()

        else:
            print("Toprak nemi yeterli. Sulamaya gerek yok.")
            self.sulama_sistemi.kapa()


# ----------------------------------
# ANA PROGRAM
# ----------------------------------

sicaklik_sensoru = SicaklikSensoru("Sıcaklık Sensörü", 35)
nem_sensoru = NemSensoru("Nem Sensörü", 23)
sulama_sistemi = SulamaSistemi("Ana Sulama Sistemi", 6)

kontrol = SulamaKontrol(
    sicaklik_sensoru,
    nem_sensoru,
    sulama_sistemi
)

# Sensörleri çalıştır
sicaklik_sensoru.ac()
nem_sensoru.ac()

# Sensör bilgilerini göster
sicaklik_sensoru.bilgi_goster()
nem_sensoru.bilgi_goster()

# Otomatik sulama kontrolü
kontrol.otomatik_kontrol()
