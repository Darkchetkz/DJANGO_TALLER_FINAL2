# Generated by Django 4.1.3 on 2022-12-15 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminarioapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instituciones',
            old_name='nombre',
            new_name='nombrep',
        ),
        migrations.RenameField(
            model_name='instituciones',
            old_name='run',
            new_name='rutp',
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='Fec_inscripcion',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='Num_telefono',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='hora',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='rutP',
            field=models.CharField(max_length=12),
        ),
    ]
