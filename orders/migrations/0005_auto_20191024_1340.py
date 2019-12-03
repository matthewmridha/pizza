# Generated by Django 2.2.6 on 2019-10-24 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20191024_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(max_length=120)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
