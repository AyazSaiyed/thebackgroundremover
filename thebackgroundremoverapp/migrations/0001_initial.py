# Generated by Django 2.1.1 on 2019-07-08 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imageupload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernamea', models.TextField(max_length=30)),
                ('uploadedimage', models.ImageField(upload_to='uploadedimages')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=30)),
                ('image', models.ImageField(upload_to='images')),
                ('useremail', models.EmailField(blank=True, max_length=254)),
                ('userpassword', models.TextField()),
                ('userphone', models.TextField(max_length=10)),
            ],
        ),
    ]
