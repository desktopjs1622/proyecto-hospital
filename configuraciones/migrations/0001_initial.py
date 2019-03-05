# Generated by Django 2.1.7 on 2019-03-05 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
        migrations.CreateModel(
            name='SistemaAparatoBiologico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_aparato', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Sistema o Aparato Biologico',
                'verbose_name_plural': 'Sistema o Aparato Biologico',
                'db_table': 'sistema_aparato_biologico',
                'ordering': ['nombre_aparato'],
            },
        ),
    ]
