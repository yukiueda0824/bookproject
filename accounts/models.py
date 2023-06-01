from django.db import models
from django.conf import settings

# Create your models here.
CATEGORY = (('ビジネス', 'ビジネス'), ('生活', '生活'), ('その他', 'その他'),
            ('システム','システム'),('ウェブ','ウェブ'),('インフラ','インフラ'),('上流工程','上流工程'),
            ('プログラミング言語','プログラミング言語'),('PC関連','PC関連'),('ゲーム開発','ゲーム開発'),
            ('デザイン開発','デザイン開発'),('外国語','外国語'),)
GENDER_CHOICE = [(None, "--"), ("男性", "男性"), ("女性", "女性")]

class Myprofile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,default="profile")
    name = models.CharField(max_length=100,verbose_name="名前")
    gender = models.CharField(max_length=2, choices=GENDER_CHOICE, default=None, verbose_name="性別", blank=True, null=True)
    book = models.CharField(max_length=100, verbose_name="お気に入りの本")
    interestedcategory = models.CharField(
        max_length=100,
        choices = CATEGORY,
        verbose_name="興味あるカテゴリ"
    )
    experiencedcategory = models.CharField(
        max_length=100,
        choices = CATEGORY,
        verbose_name="経験あるカテゴリ"
    )
    joingtime = models.DateField(blank=True, null=True,verbose_name="入社日")
    text = models.TextField(blank=True, null=True,verbose_name="自己紹介")
    def __str__(self):
        return self.title