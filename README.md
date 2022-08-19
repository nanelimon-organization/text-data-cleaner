<h1 align = 'Center'>Veri Temizleme Aracı</h1>

  ![plot](./static/img/ekran.jpeg)

Veriseti oluşturulduktan sonra modellemeye hazırlık aşaması olarak veri ön işleme adımı modelin başarısı için çok önemlidir.
Bu nedenle mutlaka her modelleme öncesi veriler temizlenmelidir. 
Metin verisi temizleme işlemi doğal dil işleme yapan herkesin her modelleme öncesinde yaptığı ve önemli olan bir adım olmasından dolayı,
Türkçe metinlerde doğal dil işleme alanında literatüre katkı olarak **text-data-cleaner** aracı geliştirilmiştir.
Veri temizleme öncesi herkesçe kullanılabilecek basit bir araçtır.

[Heroku bulut tabanlı platform servisi](https://www.heroku.com/about#:~:text=Heroku%20is%20a%20container%2Dbased,getting%20their%20apps%20to%20market.) kullanılarak ücretsiz bir şekilde  kullanıma açılmıştır..

[araç linki](https://text-data-cleaner.herokuapp.com/)

#### Aracın kullanımını anlatan video için [buraya tıklayın.](https://youtu.be/osjWOwDcqvQ)

# Ortam Oluşturma

Lütfen Python sürümünüzü '3.10' olarak ayarlayın.

Python versiyonunuzdan emin olmak için:

```bash
python3 --version
```

## Geliştirme Ortamını Ayarlamak
- Virtual environment oluşturunuz.
```bash
    $ python -m venv <venv-name>
```
- Virtual environmentınızı aktive ediniz.
```bash
    $ source <venv-name>/bin/activate
```
- Kütüphaneleri Yükleyiniz.
```bash
    $ pip install -r requirements.txt
```

# Çalıştırma

Uygulamanın çalışması için gerekli adımlar tamamlanmıştır.

```bash
    $ python3 wsgi.py
```

App 8000 portunda çalışmaktadır.
> http://localhost:8000/ 



