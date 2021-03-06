# Generated by Django 3.2.3 on 2021-06-01 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('generalmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='utils.generalmodel')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, help_text='Descripción corta', null=True)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
            bases=('utils.generalmodel', models.Model),
        ),
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('generalmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='utils.generalmodel')),
                ('title', models.CharField(max_length=150)),
                ('resume', models.TextField(blank=True, help_text='Resumen', null=True)),
                ('publication_date', models.DateField()),
                ('cover_page', models.ImageField(blank=True, null=True, upload_to='portadas')),
                ('authors', models.ManyToManyField(to='author.AuthorModel')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_categ', to='book.categorymodel')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
            bases=('utils.generalmodel',),
        ),
    ]
