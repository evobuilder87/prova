# Generated by Django 3.2.9 on 2021-12-08 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LVapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immagine', models.ImageField(upload_to='')),
                ('nome', models.CharField(max_length=20)),
                ('prezzo', models.FloatField()),
            ],
        ),
    ]