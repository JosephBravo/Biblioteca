# Generated by Django 2.0.13 on 2019-05-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0005_delete_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['nombre_categoria'],
            },
        ),
    ]