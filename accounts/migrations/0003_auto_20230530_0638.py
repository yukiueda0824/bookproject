# Generated by Django 3.2 on 2023-05-30 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_myprofile_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[(None, '--'), ('m', '男性'), ('f', '女性')], default=None, max_length=1, null=True, verbose_name='性別'),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='book',
            field=models.CharField(max_length=100, verbose_name='お気に入りの本'),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='experiencedcategory',
            field=models.CharField(choices=[('business', 'ビジネス'), ('life', '生活'), ('other', 'その他'), ('system', 'システム'), ('web', 'ウェブ'), ('infrastructure', 'インフラ'), ('upstreamprocess', '上流工程'), ('programminglanguage', 'プログラミング言語'), ('PCrelated', 'PC関連'), ('game', 'ゲーム開発'), ('design', 'デザイン開発'), ('foreignlanguage', '外国語')], max_length=100, verbose_name='経験あるカテゴリ'),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='interestedcategory',
            field=models.CharField(choices=[('business', 'ビジネス'), ('life', '生活'), ('other', 'その他'), ('system', 'システム'), ('web', 'ウェブ'), ('infrastructure', 'インフラ'), ('upstreamprocess', '上流工程'), ('programminglanguage', 'プログラミング言語'), ('PCrelated', 'PC関連'), ('game', 'ゲーム開発'), ('design', 'デザイン開発'), ('foreignlanguage', '外国語')], max_length=100, verbose_name='興味あるカテゴリ'),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='joingtime',
            field=models.DateField(blank=True, null=True, verbose_name='入社日'),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='name',
            field=models.CharField(max_length=100, verbose_name='名前'),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='自己紹介'),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]