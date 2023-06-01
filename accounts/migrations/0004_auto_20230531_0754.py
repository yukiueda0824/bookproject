# Generated by Django 3.2 on 2023-05-31 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20230530_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='experiencedcategory',
            field=models.CharField(choices=[('ビジネス', 'ビジネス'), ('生活', '生活'), ('その他', 'その他'), ('システム', 'システム'), ('ウェブ', 'ウェブ'), ('インフラ', 'インフラ'), ('上流工程', '上流工程'), ('プログラミング言語', 'プログラミング言語'), ('PC関連', 'PC関連'), ('ゲーム開発', 'ゲーム開発'), ('デザイン開発', 'デザイン開発'), ('外国語', '外国語')], max_length=100, verbose_name='経験あるカテゴリ'),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[(None, '--'), ('男性', '男性'), ('女性', '女性')], default=None, max_length=2, null=True, verbose_name='性別'),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='interestedcategory',
            field=models.CharField(choices=[('ビジネス', 'ビジネス'), ('生活', '生活'), ('その他', 'その他'), ('システム', 'システム'), ('ウェブ', 'ウェブ'), ('インフラ', 'インフラ'), ('上流工程', '上流工程'), ('プログラミング言語', 'プログラミング言語'), ('PC関連', 'PC関連'), ('ゲーム開発', 'ゲーム開発'), ('デザイン開発', 'デザイン開発'), ('外国語', '外国語')], max_length=100, verbose_name='興味あるカテゴリ'),
        ),
    ]
