# Toprak Temelli Ürün Önerisi

Bu proje, toprak özelliklerine dayalı olarak en uygun tarım ürününü tahmin eden bir sistem geliştirmek amacıyla hazırlanmıştır. Yapay zeka destekli bu uygulama sayesinde, çiftçiler tarımsal kararlarını veriye dayalı şekilde alabilir, böylece daha verimli ve sürdürülebilir bir üretim süreci oluşturulabilir.

## Proje Amacı

Geleneksel yöntemlerin ötesine geçerek, toprak analizine dayalı otomatik ürün önerileri sunmak hedeflenmiştir. Proje kapsamında geliştirilen model, belirli toprak verileri üzerinden hangi ürünün daha uygun olabileceğini tahmin eder.

## Veri Seti

Proje kapsamında Kaggle üzerinden temin edilen "Crop Recommendation Dataset" kullanılmıştır. Veri setinde aşağıdaki değişkenler yer almaktadır:

- Azot (N)  
- Fosfor (P)  
- Potasyum (K)  
- Sıcaklık (°C)  
- Nem (%)  
- pH  
- Yağış (mm)  
- Hedef değişken (Ürün adı)

Veri seti dengelidir ve eksik değer içermemektedir.

## Yöntem ve Uygulama

- Veriler temizlendikten sonra uygun şekilde ölçeklenmiştir.  
- Özellik seçimi yapılmış, model eğitimi için gerekli veriler hazırlanmıştır.  
- Farklı makine öğrenmesi algoritmaları (Random Forest, KNN, Decision Tree) ile modeller eğitilmiş ve test edilmiştir.  
- En yüksek başarıyı gösteren model seçilerek tahmin sürecine entegre edilmiştir.

## Web Arayüzü

Kullanıcıların sistemi kolayca kullanabilmesi için bir web arayüzü geliştirilmiştir. Flask tabanlı bu arayüzde kullanıcıdan gerekli toprak bilgileri alınmakta, tahmin işlemi gerçekleştirilmekte ve önerilen ürün ile birlikte görseli kullanıcıya sunulmaktadır.


## Geliştiriciler

- Ayşegül Tekeş  
- Nisa Çetinel
