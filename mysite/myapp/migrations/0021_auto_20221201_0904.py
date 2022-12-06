# Generated by Django 3.2.12 on 2022-12-01 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_auto_20221201_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='restaurants_name',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.commonmodel')),
                ('customer_name', models.CharField(max_length=100)),
                ('restaurants_id', models.ManyToManyField(related_name='restaurants', to='myapp.Restaurants')),
            ],
            bases=('myapp.commonmodel',),
        ),
    ]
