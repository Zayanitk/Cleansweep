# Generated by Django 3.2.18 on 2023-08-16 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_payment_ordermain'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(default='', max_length=100)),
                ('ORDER_MAIN', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='myapp.order_main')),
            ],
        ),
    ]
