# Generated by Django 4.1.3 on 2023-01-09 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_alter_producto_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='catalogo/'),
        ),
    ]
