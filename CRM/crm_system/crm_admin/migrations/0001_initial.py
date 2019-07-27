# Generated by Django 2.2.3 on 2019-07-23 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='salesMan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='pic')),
                ('email', models.EmailField(max_length=254)),
                ('occupation', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('address', models.TextField()),
                ('data_registration', models.DateField()),
            ],
        ),
    ]