# Generated by Django 2.2.3 on 2019-07-23 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_admin', '0002_salesman_salesman_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billId', models.IntegerField()),
                ('billDate', models.DateTimeField()),
                ('customer_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('status', models.BooleanField(verbose_name='Fales')),
                ('technician', models.CharField(max_length=50)),
                ('compline_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='customer',
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
                ('data_registration', models.DateTimeField()),
                ('customer_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('stock_status', models.BooleanField()),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('model', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='pic')),
                ('date_add', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('qty', models.FloatField()),
                ('billId', models.IntegerField()),
                ('product_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='salesManPerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salesMan_id', models.IntegerField()),
                ('totSales', models.IntegerField()),
                ('month_sale', models.IntegerField()),
                ('year_sale', models.IntegerField()),
                ('avg_sale', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='salesman',
            name='occupation',
        ),
        migrations.AddField(
            model_name='salesman',
            name='dateOfBirth',
            field=models.DateField(default='2000-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salesman',
            name='territory',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salesman',
            name='data_registration',
            field=models.DateTimeField(),
        ),
    ]