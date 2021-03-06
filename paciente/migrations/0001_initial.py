# Generated by Django 2.1.7 on 2019-03-24 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuraciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroPaciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=80)),
                ('seg_nombre', models.CharField(max_length=80)),
                ('seg_apellido', models.CharField(max_length=80)),
                ('fecha_nacimiento', models.DateField()),
                ('letra_cedula_identidad', models.CharField(blank=True, choices=[('V', 'V'), ('E', 'E')], default='V', max_length=1, null=True, verbose_name='Letra C.I.')),
                ('cedula_identidad', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Cédula de Identidad')),
                ('sexo', models.CharField(blank=True, choices=[('F', 'FEMENINO'), ('M', 'MASCULINO')], max_length=255, null=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name='fecha de registro')),
                ('registro_actualizado', models.DateTimeField(auto_now=True, verbose_name='fecha de actualizacion')),
                ('nombre_ciudad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='configuraciones.Ciudad')),
                ('nombre_estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='configuraciones.Estado')),
                ('nombre_municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='configuraciones.Municipio')),
                ('nombre_pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='configuraciones.Pais')),
                ('nombre_parroquia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='configuraciones.Parroquia')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'db_table': 'paciente"."registro_paciente',
                'ordering': ['nombre'],
            },
        ),
    ]
