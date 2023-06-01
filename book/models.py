from django.db import models
from .consts import MAX_RATE
from django.utils import dateformat
from datetime import datetime

# Create your models here.
CATEGORY = (('ビジネス', 'ビジネス'), ('生活', '生活'), ('その他', 'その他'),
            ('システム','システム'),('ウェブ','ウェブ'),('インフラ','インフラ'),('上流工程','上流工程'),
            ('プログラミング言語','プログラミング言語'),('PC関連','PC関連'),('ゲーム開発','ゲーム開発'),
            ('デザイン開発','デザイン開発'),('外国語','外国語'),)
RATE_CHOISE = [(x, str(x)) for x in range(0, MAX_RATE + 1)]
d = datetime.now()
dt_now =dateformat.format(d, 'Y-n-d')

class Book(models.Model):
    title = models.CharField(max_length=100,verbose_name="本のタイトル")
    text = models.TextField(verbose_name="本の説明")
    thumbnail = models.ImageField(null=True, blank=True,verbose_name="画像")
    category = models.CharField(
        max_length=100,
        choices = CATEGORY,
        verbose_name="カテゴリ"
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name="レビュータイトル")
    text = models.TextField(verbose_name="レビュー内容")
    rate = models.IntegerField(choices=RATE_CHOISE,verbose_name="評価")
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    time = models.DateField(blank=True, null=True, default=dt_now, verbose_name="投稿時間")

    def __str__(self):
        return self.title

