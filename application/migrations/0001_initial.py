# Generated by Django 5.0.6 on 2024-06-13 02:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tuition', '0002_tuitionpost_creation_time'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('tuition_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuition.tuitionpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
