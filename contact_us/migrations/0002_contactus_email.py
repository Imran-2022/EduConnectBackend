# Generated by Django 5.0.6 on 2024-10-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.EmailField(default='example@gmail.com', max_length=254),
        ),
    ]
