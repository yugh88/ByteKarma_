# Generated by Django 5.0.7 on 2024-08-07 00:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('slug', models.SlugField(default='')),
                ('users', models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
