# Generated by Django 4.0.1 on 2022-04-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Website_Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('type_of_user', models.CharField(max_length=20)),
            ],
        ),
    ]
