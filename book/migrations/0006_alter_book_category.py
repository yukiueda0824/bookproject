# Generated by Django 3.2 on 2023-05-30 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_book_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('business', 'ビジネス'), ('life', '生活'), ('other', 'その他'), ('system', 'システム'), ('web', 'ウェブ'), ('infrastructure', 'インフラ'), ('upstreamprocess', '上流工程'), ('programminglanguage', 'プログラミング言語'), ('PCrelated', 'PC関連'), ('game', 'ゲーム開発'), ('design', 'デザイン開発'), ('foreignlanguage', '外国語')], max_length=100),
        ),
    ]
