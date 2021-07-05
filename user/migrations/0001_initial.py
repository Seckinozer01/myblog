# Generated by Django 3.1.7 on 2021-05-16 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hesap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='E-posta')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Kullanıcı Adı')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Son Oturum')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
