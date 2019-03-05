# Generated by Django 2.1.7 on 2019-03-05 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatologiasGenerales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_patologico', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Patologia',
                'verbose_name_plural': 'Patologias o Enfermedades',
                'db_table': 'listado_general_patologico',
                'ordering': ['nombre_patologico'],
            },
        ),
        migrations.CreateModel(
            name='PreguntaSecreta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Pregunta Secreta',
                'verbose_name_plural': 'Preguntas Secretas',
                'db_table': 'pregunta_secreta',
                'ordering': ['nombre'],
            },
        ),
    ]
