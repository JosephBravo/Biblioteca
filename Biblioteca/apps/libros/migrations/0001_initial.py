# Generated by Django 2.0.13 on 2019-05-20 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=250)),
                ('subtitulo', models.CharField(max_length=250)),
                ('autor', models.CharField(max_length=250)),
                ('categoria', models.CharField(max_length=250)),
                ('fecha_publicacion', models.DateField()),
                ('editor', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['titulo'],
            },
        ),
    ]
