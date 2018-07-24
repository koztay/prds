# coding=utf-8
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify
from utils import thumbnail_creator


# Create your models here.
def thumbnail_location(instance, filename):
    return "site_images/%s/thumbnails/%s" % (instance.slider.slug, filename)  # bunu sadece slider için kullanabiliyoruz


# This utility function creates the filename and filepath according to the slug and product instance
def image_upload_to(instance, filename):
    title = instance.title
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" % (slug, instance.id, file_extension)
    return "site_images/%s/%s" % (slug, new_filename)


class SliderImage(models.Model):
    """
    Bu sınıf anasayfadaki en üstte çıkan en büyük resimlerin olduğu sliderları yönetmek için.
    """
    type_choices = (
        ("Tip1", "tip1"),
        ("Tip2", "tip2"),
    )

    title = models.CharField(max_length=120)  # bu o slide  için en büyük başlık
    description = models.CharField(max_length=400, null=True, blank=True)  # bu kısa açıklama
    slug = models.SlugField(blank=True, )  # bu olmadan thumbnail yaratamıyor gerzek
    image = models.ImageField(upload_to=image_upload_to)  # slider size 1280x850 ve 500x333 ebatında.
    url = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    siralama = models.IntegerField(default=0)
    tip = models.CharField(max_length=10, choices=type_choices)

    def get_image_path(self): # Buna gerek olmayabilir, çünkü kesme biçme yok, ama ileride
        # onu da yapmak gerekebilir... O nednele şimdilik kalsın...
        # img = self.image

        img_url = self.image.url
        # remove MEDIA_URL from img_url
        img_url = img_url.replace(settings.MEDIA_URL, "/", 1)
        # combine with media_root
        img_path = settings.MEDIA_ROOT + img_url
        if img_url:
            return img_path
        return img_path  # None

    def __str__(self):
        return self.title


SLIDER_THUMB_CHOICES = (
    ("lg", "Large"),  # 450x450
    ("md", "Medium"),  # 300x220
)


class SliderImageTextFields(models.Model):
    image = models.ForeignKey(SliderImage)
    icon = models.CharField(max_length=20, null=True, blank=True)
    text = models.CharField(max_length=100, null=True, blank=True)
    siralama = models.IntegerField(default=0)

    def __str__(self):
        return "Sıralama: {}, Image: {}".format(self.siralama, self.image.title)

    class Meta:
        ordering = ('siralama', )


class SliderThumbnail(models.Model):
    slider = models.ForeignKey(SliderImage)  # instance.promotion.title
    type = models.CharField(max_length=20, choices=SLIDER_THUMB_CHOICES, default='lg')
    height = models.CharField(max_length=20, null=True, blank=True)
    width = models.CharField(max_length=20, null=True, blank=True)
    media = models.ImageField(
        width_field="width",
        height_field="height",
        blank=True,
        null=True,
        upload_to=thumbnail_location)

    def __str__(self):  # __str__(self):
        return str(self.media.path)


# works when a slider object has been saved for creating slider thumbnails
def slider_post_save_receiver_for_thumbnail(sender, instance, created, *args, **kwargs):
    if sender:  # bu ilk seferde neden None döndürüyor anlamadım?
        hd, hd_created = SliderThumbnail.objects.get_or_create(slider=instance, type='lg')
        sd, sd_created = SliderThumbnail.objects.get_or_create(slider=instance, type='md')

        lg_max = (1280, 850)
        md_max = (500, 333)

        media_path = instance.get_image_path()
        owner_slug = instance.slug
        """
        eğer thumnail objesi yoksa ilk defa yaratılıyorsa o zaman imajları set ediyoruz. Buradaki sıkıntı şu: resmi
        değiştirdiğimiz zaman o zaman thumbnail yaratamıyoruz. Fakat if içerisine de almazsak o zaman her seferinde
        thumbnail yaratıyoruz, yani başlığı bile değiştirsek. Bunu nasıl çözeceğiz anlamadım? Image field için ayrı
        bir model yaratarak çözebiliriz belki...
        """
        if hd_created:
            thumbnail_creator.create_new_thumb(media_path, hd, owner_slug, lg_max[0], lg_max[1])

        if sd_created:
            thumbnail_creator.create_new_thumb(media_path, sd, owner_slug, md_max[0], md_max[1])

post_save.connect(slider_post_save_receiver_for_thumbnail, sender=SliderImage)


class Testimonial(models.Model):
    name_of_person = models.CharField(max_length=120)  # yorumu yapan kişinin adı
    comment = models.TextField()
    comment_date = models.DateField()
    image = models.CharField(max_length=500)  # satın aldığı ürünün resim linki n11 'deki
    url = models.CharField(max_length=250)  # N11 veya gittigidiyordaki sayfa linki
    active = models.BooleanField(default=True)

    def __str__(self):  # __str__(self):
        return str(self.name_of_person)
