# Generated by Django 2.1.7 on 2019-04-02 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ciudad', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades de la Nacion',
                'db_table': 'configuracion"."ciudad_nacion',
                'ordering': ['nombre_ciudad'],
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estado', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados de la Nacion',
                'db_table': 'configuracion"."estado_nacion',
                'ordering': ['nombre_estado'],
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_municipio', models.CharField(max_length=255)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='configuraciones.Estado')),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipios de la Nacion',
                'db_table': 'configuracion"."municipio_nacion',
                'ordering': ['nombre_municipio'],
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pais', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Pais Nacion',
                'verbose_name_plural': 'Nacionalidad',
                'db_table': 'configuracion"."pais_nacion',
                'ordering': ['nombre_pais'],
            },
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_parroquia', models.CharField(max_length=255)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='configuraciones.Municipio')),
            ],
            options={
                'verbose_name': 'Parroquia',
                'verbose_name_plural': 'Parroquias de la Nacion',
                'db_table': 'configuracion"."parroquia_nacion',
                'ordering': ['nombre_parroquia'],
            },
        ),
        migrations.CreateModel(
            name='PatologiasGenerales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_patologico', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Patologia',
                'verbose_name_plural': 'Patologias o Enfermedades',
                'db_table': 'configuracion"."listado_general_patologico',
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
                'db_table': 'configuracion"."pregunta_secreta',
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
                'db_table': 'configuracion"."sistema_aparato_biologico',
                'ordering': ['nombre_aparato'],
            },
        ),
        migrations.AddField(
            model_name='patologiasgenerales',
            name='aparato_biologico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='configuraciones.SistemaAparatoBiologico'),
        ),
        migrations.AddField(
            model_name='estado',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='configuraciones.Pais'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='configuraciones.Municipio'),
        ),
    ]