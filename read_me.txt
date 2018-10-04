
2 adet brach olmalı burada sebebi ise birincisi github 'a gönderilen origin branchı
Diğeri ise remote file server 'a gönderilen branch. Aradaki fark github 'a gönderdiğimizde .env ignore listesinde,
diğerinde ise ignore listesinde değil.

diğer brach ile çalışırken add remote yapınca aynı remote 'dosyasını git'e push ediyor mu acaba? deneyip
göreceğiz...

git remote add production ssh://kemal@139.162.180.219/var/git/pureads.git komutu ile remote repo oluşturuyoruz ve

bir de ne görelim aşağıdaki gibi bir hata:
fatal: remote production already exists.

bunun için aşağıdaki komutu verdik :
git remote rm production

sonrasında tekrardan
git remote add production ssh://139.162.180.219:/var/git/pureads.git
komutu ile remote eklemesi yapmış olduk.

şimdi
git push production
dediğimizde sıçmaması gerek ama ne görelim sıçtı aşağıdaki komutu ver dedi:

git push --set-upstream production production_server

verdik ama yine sıçtık. Şimdi de şu hatayı verdi:

fatal: '/var/git/pureads' does not appear to be a git repository
fatal: Could not read from remote repository.

demek ki repo yok. O nedenle deploy -a demek gerek sanırım ki dosyalar kopyalansın.
cd deploy ile klasöre girip diyelim bakalım.

./deploy.sh -a
ile tüm deploy procesini baştan aldık...

sonra tekrar aynı komut:
git push --set-upstream production production_server

yine hatalar hatalar:
remote: fatal: You are on a branch yet to be born
remote: .IOError: [Errno 2] No such file or directory: '/var/git/pureads/docker-compose.yml'
remote: .IOError: [Errno 2] No such file or directory: '/var/git/pureads/docker-compose.yml'

bir daha git push de bakalım ne olacak bu sefer sadece git push production diyorum:
git push production

şimdi de herşey update dedi:
Everything up-to-date

Hata master 'ı push etmiyor olmamızdan kaynaklanıyor. master branch 'ı push edince oldu.

ayrıca master bracha push ettiğimiz de bildirmemizi istiyor yani :
git push production master
şeklinde olunca oluyor.

sonrasında ssh ile login olup
cd /var/git/pureads klasörüne giriyoruz

docker-compose run django python manage.py makemigrations (app/manage.py yazmadan çalışıyor yazınca bulamıyor.)
docker-compose run django python manage.py migrate

komutları ile veritabanını güncelliyoruz...

github 'daki origine push ederken ise .env 'yi gitignore dosyasına eklemeliyiz.
ekleyince aşağıdaki komutu ver:
git rm --cached --force .env
fatal: pathspec '.env' did not match any files
hatasını veriyor ama origine push etmeyecek.


bannerların üzetini kaplayan filtre
banner_type_1 or _2 line 10 : => <div class="tp-caption dark-translucent-background"

da7ad7115f36150b70fdec1d2f82bbf4e8689da2 (HEAD -> master, origin/master) bazı resnler çıkartıldı.
78e77b0aa635e01a77a5ce17eca9745eeb1ed237 bazı resnler çıkartıldı.
b7a1e412c157d51463c16ecd7dc65d7ba2052e93 backup alındı
f540d723e1df564b1951c782941bc12f6917853b (production/master) href linklerinden class kaldırıldı.
aad5e5c04e5b5f6ba9c54d2047b7bde80417cd76 modernizr javascript kodları kaldırıldı.
8562704c7398ded9c21f97cd07320fe66da2e8d4 inline links + hurriyet logo
b9d445b1ee5bd35e194bb408636eab240c58bf07 deleted env file
324bb290757ff37f592ed6e1e8fc449267d2b250 yayincilarimiz ve blog eklendi.
40066104ab251c5f88b560fc3e554c81e5d3424d anasayfa linkleri düzeltildi.
6915d48d5084ebb9f27f98cf5d64cc5673a25bcc IP adresi eklendi.
c79bfec9c7b151e230c9e12f72d413b0e67f5242 yeni server düzenlemeleri
8156523be68dfa1d257bd2974c16ec9a5b3e90a5 modified IP address
54ccd63d2409974eac68466be7cc87896057fa1c postgres 9.4 e döndü.
4853161d6ef593868eae357b5301d430b6959031 revizeler
9d043a281925cd0f3569730c57fa36b400b6735f menü yapıldı.
4388f138658d016cf0834fc776d29dff9c6cb1b7 revizyonlara devam
68fdd3f111fedb92806d094ccd914bc641b30f4f slider duration değiştirldi.
fb8071c9c57905cca3c60918b8830ff4dbe461f8 düzletmeler, düzeltmeler...
4e7c91d3df2f4572d68df7234d1aa1b6a3e418ac admin url düzeltildi
a2c0ae6e21ae2d22b6437c74f2bf007c746ceec9 revizyonlar yapıldı.
:
