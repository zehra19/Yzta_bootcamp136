# 🧠 TUScope – TUS Çıkmış Soru ve Spot Bilgi Asistanı


<p align="center">
  <img src="https://github.com/zehra19/Yzta_bootcamp136/blob/main/assets/TUScope.png" alt="TUScope Logo" width="250"/>
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
📎 Whatsapp üzerinden iletişim kurduk. Görev dağılımlarını yaptık  [https://github.com/zehra19/Yzta_bootcamp136/blob/main/assets/Ekran%20Resmi%202025-07-09%2018.14.55.png]
📎[https://github.com/zehra19/Yzta_bootcamp136/blob/main/assets/Ekran%20Resmi%202025-07-06%2023.32.35.png]

## Sprint Board (Trello / Miro):
📎   [https://github.com/zehra19/Yzta_bootcamp136/blob/main/assets/sprint%20board.png]

##  Ürün Ekran Görüntüsü (Taslak):
📎 [https://github.com/zehra19/Yzta_bootcamp136/blob/main/assets/spot_ekran.png]

---

##  Sprint Review:
- Fikrin teknik uygulanabilirliği doğrulandı.
- GPT entegrasyonu hızlı ve başarılı sonuç verdi.
- JSON modeli projeye esneklik kazandırıyor.
- Jüri sunumuna uygun, sade ve güçlü bir yapı kuruluyor.

## Sprint Retrospektif:
- Takım içi iletişim kuvvetliydi.
- Roller doğru paylaşıldı, sprint planına sadık kal


## 📌 Sprint 2 - Görev Dağılımı ve Takibi

### 🎯 Amaç
Kullanıcının filtreleme, istatistiksel veri görüntüleme, spot bilgi alma ve geri bildirim sağlama işlemlerini gerçekleştirebildiği daha fonksiyonel bir arayüz oluşturmak.

---

### ✅ Görev Tablosu

| No  | Görev Adı                                                       | Atanan Kişi | Açıklama                                                                                                                                               | Durum         |
|-----|------------------------------------------------------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| 1   | Konu Bazlı Soru Filtreleme Özelliği                             | Zehra       | Kullanıcının JSON verisi üzerinden soruları konuya göre filtreleyebilmesi sağlandı. Arayüze filtre seçenekleri eklendi.                              | ✅ Tamamlandı |
| 2   | Streamlit Üzerinde Konu Bazlı Soru Listeleme Sayfası            | Yasemin     | Kullanıcı filtreleme sonrası sadece ilgili soruları görebilecek. Sayfa tasarımı ve veri çekimi tamamlandı.                                           | ✅ Tamamlandı |
| 3   | İstatistiksel Özelliklerin Hazırlanması                         | Furkan      | JSON üzerinden toplam soru sayısı, doğru cevap oranı gibi temel istatistiksel bilgiler çıkarıldı.                                                    | ✅ Tamamlandı |
| 4   | Spot Bilgi Alanının Dinamik Hale Getirilmesi                    | Furkan      | Spot bilgiler ayrı bir dosyadan çekilecek. Soru ile ilişkili bilgiler kullanıcıya gösterilecek.                                                       | 🔄 Devam Ediyor |
| 5   | Kullanıcı Geri Bildirim Butonu Oluşturulması                    | Zehra       | Kullanıcılar sorular hakkında yorum ya da geri bildirim bırakabilecek. Streamlit butonlarıyla geliştirilecek.                                        | ⏳ Başlanacak |
| 6   | README Dosyasının Güncellenmesi                                 | Yasemin     | Yeni özellikler, görev dağılımı ve kurulum bilgileri README dosyasına eklenecek.                                                                      | ⏳ Başlanacak |
| 7   | PDF Çıktısı Geliştirme (Ekstra Görev - Sprint Board'dan)        | Zehra       | Kullanıcının içerikleri PDF olarak indirebilmesi için çıktı sistemi geliştirilecek.                                                                  | ⏳ To Do       |

---

### 📊 Sprint Panosu

| Durum            | Görevler                                                                                 |
|------------------|-------------------------------------------------------------------------------------------|
| ✅ **Done**       | Konu bazlı filtreleme arayüzü, Soru listeleme sayfası, İstatistiksel analiz altyapısı    |
| 🔄 **In Progress**| Spot bilgi üretimi ekranı (Furkan)                                                        |
| ⏳ **To Do**      | Geri bildirim butonu (Zehra), README güncellemesi (Yasemin), PDF çıktısı geliştirme (Zehra) |

---
## 📊 Tahmin Edilen Puan ve Tamamlanan Puan

| Görev                                              | Atanan  | Tahmini Puan | Tamamlanan Puan |
|----------------------------------------------------|---------|---------------|------------------|
| Konu Bazlı Soru Filtreleme                         | Zehra   | 3             | 3                |
| Konu Bazlı Listeleme Sayfası                       | Yasemin | 2             | 2                |
| İstatistiksel Verilerin Çıkarılması                | Furkan  | 3             | 3                |
| Spot Bilgi Ekranı                                   | Furkan  | 5             | 3                |
| Geri Bildirim Butonu                               | Zehra   | 2             | 0                |
| README Güncellemesi                                | Yasemin | 1             | 0                |
| PDF Çıktısı Özelliği                               | Zehra   | 2             | 0                |

> 🧮 **Toplam Tahmini Puan:** 18  
> ✅ **Tamamlanan Puan:** 11  
> 🔺 **Tamamlanma Oranı:** %61

---

## 📘 Puan Tamamlama Mantığı
- Her görev için puanlar, zorluk derecesine göre Scrum puanlaması ile (Fibonacci veya basit sayı sistemi) belirlendi.
- Tamamlanan her görev, görev kartı tamamlandı olarak işaretlenince sprint puanına eklendi.
- Yarım kalan görevlerin puanı sayılmadı.

---

### 👥 Katılımcılar

| İsim     | Sorumluluklar                                                                 |
|----------|--------------------------------------------------------------------------------|
| **Zehra**   | Filtreleme arayüzü, kullanıcı geri bildirimi, PDF çıktısı geliştirme          |
| **Yasemin** | Soru listeleme sayfası, README güncelleme                                    |
| **Furkan**  | Spot bilgi ekranı, istatistiksel veri işleme                                 |


## 🗓️ Daily Scrum Görseli:

📎 Herkes görev dağılımına göre işlerini halletti.  

📎 [https://github.com/zehra19/Yzta_bootcamp136/blob/main/assets/sprintt2.jpg]



## 📌 Sprint Board (Trello / Miro):

[Sprint Board Görseli]

📎 [https://github.com/zehra19/Yzta_bootcamp136/blob/main/assets/sprint%202%20board.png]

📎 [https://github.com/zehra19/Yzta_bootcamp136/blob/main/assets/sprint%202.png]



## 🔁 Sprint 2 Retrospektif:

- Görev dağılımları Sprint planına göre sürdü.
- Zaman yönetimi bazı alanlarda sıkıştı, PDF ve test süreci Sprint 3'e taşınabilir.
- Takım içi iletişim güçlüydü, teknik destek hızlı sağlandı.


# 🏆 Sprint 3 - TUScope Mini (Final Sprint)

Merhaba! Ben **Yasemin** 👋  
Bu sprint, **TUScope Mini** projesinin **son sprinti** oldu.  
Amacım, TUS’a hazırlanan öğrenciler için 7 ana ders kategorisinde spot bilgiler ve mini testler sunan interaktif bir uygulamayı tamamlamaktı.  

---

## 📌 Sprint 3 Hedeflerim
- 7 bölümlük quiz sistemini tamamlamak  
- Spot bilgileri eklemek  
- Doğru/yanlış geri bildirimleri ve doğru sayısı göstermek  
- Streamlit arayüzünü son hâline getirmek  
- Uygulamayı test edip ekran görüntüleri almak  

---

## 🛠️ Yaptıklarım ve Puanlamam

### 1️⃣ 7 Bölümlük Quiz Sistemi Kurulumu (25/25)
- **Yaptığım İş:**  
  - Anatomi, Biyokimya, Fizyoloji, Farmakoloji, Mikrobiyoloji, Patoloji ve Histoloji olmak üzere **7 bölüm** ekledim.  
  - Her bölüm için **2 soru** olacak şekilde mini quizler tasarladım.  
- **Sonuç:** Kullanıcılar istediği bölümü seçip iki soruluk mini testi çözebiliyor.  
- **Puan:** ✅ 25/25

---

### 2️⃣ Spot Bilgiler Ekleme (15/15)
- **Yaptığım İş:**  
  - Her dersin başına, soruları çözmeden önce hızlıca gözden geçirilebilecek **spot bilgiler** ekledim.  
  - Örnek:  
    - *Farmakoloji:* “Parasempatolitikler asetilkolin etkisini gösterir.”  
- **Puan:** ✅ 15/15

---

### 3️⃣ Doğru/Yanlış Geri Bildirimi ve Skor (20/20)
- **Yaptığım İş:**  
  - Kullanıcı bir cevabı seçtiğinde anında **Doğru!** veya **Yanlış!** mesajı gösteriliyor.  
  - Yanlışsa doğru cevabı da gösterdim.  
  - Quiz sonunda **Toplam Doğru Sayısı** ekledim.  
- **Puan:** ✅ 20/20

---

### 4️⃣ Streamlit Arayüzü ve Kullanıcı Deneyimi (20/20)
- **Yaptığım İş:**  
  - Dropdown menü ile **bölüm seçimi**  
  - Doğru cevapta **yeşil kutu**, yanlış cevapta **kırmızı kutu**  
  - Temiz ve minimal bir tasarım  
- **Puan:** ✅ 20/20

---

### 5️⃣ Test ve Ekran Görüntüleri (10/10)
- **Yaptığım İş:**  
  - Tüm uygulamayı test ettim ve soruların doğru/yanlış çalıştığını kontrol ettim.  
  - **3 farklı ekran görüntüsü** aldım ve README’ye ekledim.  
- **Puan:** ✅ 10/10

---

## 📊 Sprint 3 Toplam Puan
**90/90 ✅**  
Bu sprint ile TUScope Mini projesi tamamlandı! 🎉  

---

## 📸 Ekran Görüntüleri

### Uygulama'nın Terminelde açılımı
[Uygulama Açılımı] 

📎 [https://github.com/zehra19/Yzta_bootcamp136/blob/main/assets/Ekran%20Resmi%202025-08-02%2001.45.01.png]
📎 [https://github.com/zehra19/Yzta_bootcamp136/commit/dae213cf5db5c91e5972d557890e9864f772910b]

### 7 Bölüm Arayüzü

[TUScope Mini]
[Uygulama Bölümleri]
📎 [https://github.com/zehra19/Yzta_bootcamp136/commit/aca00020c76177cc895ed5b7a31ccea26093a130]
📎 [https://github.com/zehra19/Yzta_bootcamp136/commit/9901b93faf387b9897e138e35a6108c2d83386a6]

---

## 🚀 Uygulamayı Çalıştırmak

```bash
streamlit run TUScopeMini.py
```

Tarayıcıda açılacak: **http://localhost:8501**  

---


<p align="center">
  <img src="https://github.com/zehra19/Yzta_bootcamp136/commit/90b9f7df3406471dc4df858abc6503e3032f8059" alt="TUScope Logo" width="250"/>
</p>

<h1 align="center">🧠 TUScope</h1>
<p align="center">Uygulama Açılış</p>

### 📝 Yasemin’in Sprint 3 Notu
Bu sprintte projenin tüm hedefleri tamamlandı:  
- 7 bölümlük quiz sistemi  
- Spot bilgiler  
- Doğru/yanlış geri bildirimleri  
- Skor hesaplama  
- Arayüz ve testler  

TUScope Mini artık **kullanıma hazır** ✅



