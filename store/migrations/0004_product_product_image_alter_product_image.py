# Generated by Django 5.0.2 on 2024-03-04 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_is_sale_product_on_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='uploads/product_image/default.png', upload_to='uploads/product_image/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='uploads/product/default.png', upload_to='uploads/product/'),
        ),
    ]
