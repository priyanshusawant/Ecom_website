# Generated by Django 4.2.7 on 2023-11-23 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_item_for_user_item_prod_code_alter_item_item_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='HISTORY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('prod_ref', models.IntegerField(default=100)),
                ('item_name', models.CharField(max_length=200)),
                ('op_type', models.CharField(max_length=100)),
            ],
        ),
    ]
