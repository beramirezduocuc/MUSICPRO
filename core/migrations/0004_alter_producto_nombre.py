# Generated by Django 4.1.5 on 2023-01-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Nombre',
            field=models.CharField(max_length=50),
        ),
    ]
