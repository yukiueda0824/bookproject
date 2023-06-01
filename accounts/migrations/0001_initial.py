# Generated by Django 3.2 on 2023-05-30 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Myprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('book', models.CharField(max_length=100)),
                ('interestedcategory', models.CharField(choices=[('business', 'ビジネス'), ('life', '生活'), ('other', 'その他'), ('system', 'システム'), ('web', 'ウェブ'), ('infrastructure', 'インフラ'), ('upstreamprocess', '上流工程'), ('programminglanguage', 'プログラミング言語'), ('PCrelated', 'PC関連'), ('game', 'ゲーム開発'), ('design', 'デザイン開発'), ('foreignlanguage', '外国語')], max_length=100)),
                ('experiencedcategory', models.CharField(choices=[('business', 'ビジネス'), ('life', '生活'), ('other', 'その他'), ('system', 'システム'), ('web', 'ウェブ'), ('infrastructure', 'インフラ'), ('upstreamprocess', '上流工程'), ('programminglanguage', 'プログラミング言語'), ('PCrelated', 'PC関連'), ('game', 'ゲーム開発'), ('design', 'デザイン開発'), ('foreignlanguage', '外国語')], max_length=100)),
                ('joingtime', models.DateField()),
                ('text', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
