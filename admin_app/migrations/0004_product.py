# Generated by Django 3.1.2 on 2020-11-08 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0003_user_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.CharField(max_length=250)),
            ],
        ),
    ]
