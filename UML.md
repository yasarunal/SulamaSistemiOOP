
# UML Sınıf Diyagramı

Bu diyagram, Akıllı Sulama Sistemi projesinin
nesne yönelimli sınıf yapısını göstermektedir.

## Sınıf Diyagramı

```mermaid
classDiagram
    class Device {
        +name
        +aktif
        +ac()
        +kapa()
        +durum_goster()
    }

    class SicaklikSensoru {
        -__sicaklik
        +sicaklik_oku()
        +sicaklik_guncelle()
        +bilgi_goster()
    }

    class NemSensoru {
        -__nem
        +nem_oku()
        +nem_guncelle()
        +bilgi_goster()
    }

    class SulamaSistemi {
        -__ayar
        +ayarla()
        +sulama_yap()
        +bilgi_goster()
    }

    class SulamaKontrol {
        +sicaklik_sensoru
        +nem_sensoru
        +sulama_sistemi
        +otomatik_kontrol()
    }

    Device <|-- SicaklikSensoru
    Device <|-- NemSensoru
    Device <|-- SulamaSistemi

    SulamaKontrol --> SicaklikSensoru
    SulamaKontrol --> NemSensoru
    SulamaKontrol --> SulamaSistemi
```

## Diyagram Açıklaması

- Device: Bütün cihazların ortak özelliklerini içerir.
- SicaklikSensoru: Sıcaklık verisini okur ve günceller.
- NemSensoru: Nem verisini okur ve günceller.
- SulamaSistemi: Sulama işlemini yönetir.
- SulamaKontrol: Sensörlerden gelen verileri değerlendirerek sulama kararını verir.

Diyagram, kalıtım ve sınıflar arası ilişkileri göstermektedir.
