
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

sonrasında ssh ile login olup
cd /var/git/pureads klasörüne giriyoruz

docker-compose run django python manage.py makemigrations (app/manage.py yazmadan çalışıyor yazınca bulamıyor.)
docker-compose run django python manage.py migrate

komutları ile veritabanını güncelliyoruz...