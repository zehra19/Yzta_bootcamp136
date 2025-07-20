# 🧠 TUScope – TUS Çıkmış Soru ve Spot Bilgi Asistanı


<p align="center">
  <img src="https://github.com/zehra19/Yzta_bootcamp136/blob/main/TUScope.png" alt="TUScope Logo" width="250"/>
</p>

<h1 align="center">🧠 TUScope</h1>
<p align="center">TUS Çıkmış Soru ve Spot Bilgi Asistanı</p>

## 👥 Takım İsmi:
**YZTA_136**

## 🧑‍🤝‍🧑 Takım Üyeleri ve Rolleri

| İsim               | Rol 1          | Rol 2        |
|--------------------|----------------|--------------|
| Yasemin Yıkılmaz   | Scrum Master   | Developer    |
| Zehra Nur Yavaşoğlu| Product Owner  | Developer    |
| Furkan Akın        | Developer      | Developer            |


## Ürün İsmi:
**TUScope**

## Ürün Fikri:
TUS sınavına hazırlanan tıp fakültesi öğrencilerine, belirli bir tıbbi konu başlığı altında:
- Geçmiş yıllarda çıkmış TUS sorularını (cevaplarıyla birlikte),
- O konuya dair spot (kısa, öz) bilgileri,
- Soru çıkma istatistiklerini
bir arada sunan, AI destekli bir öğrenme asistanı.

##  Ürün Özellikleri:
- Konuya göre çıkmış TUS sorularını filtreleme
- Konuya özel GPT ile üretilmiş 5 spot bilgi
- PDF çıktı alma
- Soru-çıkarma istatistiği (opsiyonel)
- Web arayüzü üzerinden kolay kullanım

## Hedef Kitle:
- Türkiye'de TUS sınavına hazırlanan 5. ve 6. sınıf tıp fakültesi öğrencileri
- TUS’a tekrar hazırlanan mezun doktorlar

---

##  Product Backlog:

| Backlog Adımı | Açıklama | Durum |
|---------------|----------|-------|
| Kullanıcıdan konu alma | Kullanıcının bir tıbbi konu başlığı girmesi | ✅ Yapıldı |
| Spot bilgi üretme | GPT ile 5 maddelik spot bilgi oluşturma | ✅ Yapıldı |
| JSON veri modeli | Konuya göre çıkmış soru listesi (yıl/soru/cevap dahil) | ✅ Hazırlanıyor |
| Arayüz prototipi | Streamlit ekranlarının tasarımı | ✅ Başlandı |
| PDF çıktısı | Spot bilgilerin veya soruların PDF olarak indirilmesi | 🔄 Yapılacak |
| İstatistik gösterimi | Konulara göre çıkma oranı hesaplama | 🔄 Opsiyonel

---



##  Sprint 1 Notları:

- Ürün fikri kesinleşti ve ekip üyeleri rolleri benimsedi.
- GPT ile spot bilgi oluşturma test edildi.
- JSON formatında çıkmış soru verisi yapısı netleşti.
- Streamlit arayüzü temel yapısıyla başlatıldı.

## 🎯 Tahmini Puan: 50  
## ✅ Tamamlanan Puan: 30

### 🧮 Puanlama Tablosu

| Görev                          | Puan | Durum     | Açıklama                                                                 |
|-------------------------------|------|-----------|--------------------------------------------------------------------------|
| Kullanıcı girişi fikri        | 5    | ✅         | Kullanıcıdan konu alma fikri net, kodlama henüz yok.                     |
| Spot bilgi üretimi fikri      | 5    | ✅         | GPT ile spot üretimi test edildi, tam entegrasyon yapılmadı.             |
| JSON yapısı planı             | 5    | ✅         | Yapı kurgulandı, dosya içeriği henüz tamamlanmadı.                        |
| Arayüz (UI) taslak fikri      | 10   | ✅         | Streamlit üzerinden örnek ekran üretildi, fikir sunuldu.                 |
| PDF çıktısı                   | 0    | ⏳         | Planlandı ama kodlama başlamadı.                                         |
| Çıkma istatistiği (opsiyonel) | 5    | 🔄 Planlandı | Opsiyonel olarak düşünülüyor, teknik detaylar belirlenmiş değil.        |

### 🔚 Toplam: **30 / 50 Puan**


---

## Daily Scrum Görseli:
📎 Whatsapp üzerinden iletişim kurduk. Görev dağılımlarını yaptık  [https://github.com/zehra19/Yzta_bootcamp136/blob/main/Ekran%20Resmi%202025-07-09%2018.14.55.png]
📎[https://github.com/zehra19/Yzta_bootcamp136/blob/main/Ekran%20Resmi%202025-07-06%2023.32.35.png]

## Sprint Board (Trello / Miro):
📎   [https://github.com/zehra19/Yzta_bootcamp136/blob/main/sprint%20board.png]

##  Ürün Ekran Görüntüsü (Taslak):
📎 [https://github.com/zehra19/Yzta_bootcamp136/blob/main/spot_ekran.png]

---

##  Sprint Review:
- Fikrin teknik uygulanabilirliği doğrulandı.
- GPT entegrasyonu hızlı ve başarılı sonuç verdi.
- JSON modeli projeye esneklik kazandırıyor.
- Jüri sunumuna uygun, sade ve güçlü bir yapı kuruluyor.

## Sprint Retrospektif:
- Takım içi iletişim kuvvetliydi.
- Roller doğru paylaşıldı, sprint planına sadık kal


## 🚀 Sprint 2 Notları:

- GPT spot bilgi üretimi arayüz ile entegre edilmeye başlandı.
- JSON dosyasından çıkmış soru verisi arayüzde listelenmeye başlandı.
- PDF çıktısı alma ve UI düzenlemeleri planlandı.
- Projenin test süreci için temel senaryolar belirlendi.
- README güncellenerek süreç dokümante edilmeye başlandı.

### 🎯 Tahmini Puan: 50  
### ✅ Tamamlanan Puan: 20

### 🧮 Puanlama Tablosu

| Görev                     | Puan | Durum         | Açıklama                                                                 |
|---------------------------|------|---------------|--------------------------------------------------------------------------|
| GPT spot bilgi entegrasyonu | 10   | ✅ Yapıldı      | Kullanıcıdan konu alınıp GPT'den spot bilgi çekme arayüzü yazıldı.       |
| JSON veri gösterimi        | 10   | ✅ Yapıldı      | Konuya göre geçmiş TUS soruları arayüzde gösterilmeye başlandı.          |
| PDF çıktısı alma           | 10   | 🔄 Yapılıyor   | Spot bilgilerin PDF'e dönüştürülmesi planlandı, kodlamaya başlanmadı.    |
| UI düzenlemeleri           | 10   | 🔄 Yapılıyor   | Sayfa düzeni sadeleştirilecek, kullanıcı dostu tasarım uygulanacak.      |
| Test ve hata ayıklama      | 5    | 🔜 Planlandı   | Tüm özelliklerin test edilip eksiklerin belirlenmesi planlandı.          |
| README güncelleme          | 5    | 🔜 Planlandı   | Sprint 2 gelişmeleri README’ye eklenecek.                                |

### 🔚 Toplam: **20 / 50 Puan**

---

## 🗓️ Daily Scrum Görseli:

📎 Herkes görev dağılımına göre işlerini halletti.  
📎  
📎 

## 📌 Sprint Board (Trello / Miro):

📎 [Sprint Board Görseli](https://github.com/zehra19/Yzta_bootcamp136/blob/main/sprint%20board.png)

## 🖼️ Ürün Ekran Görüntüsü (Güncel Taslak):

📎 

## ✅ Sprint 2 Review:

- GPT ile anlık spot bilgi üretimi başarıyla arayüze entegre edildi.
- JSON yapıdaki soru verisi arayüzde okunabilir hale getirildi.
- Proje demo için kullanılabilecek görsel bir seviyeye ulaştı.
- Jüri sunumu için çıktılar planlandı.

## 🔁 Sprint 2 Retrospektif:

- Görev dağılımları Sprint planına göre sürdü.
- Zaman yönetimi bazı alanlarda sıkıştı, PDF ve test süreci Sprint 3'e taşınabilir.
- Takım içi iletişim güçlüydü, teknik destek hızlı sağlandı.

