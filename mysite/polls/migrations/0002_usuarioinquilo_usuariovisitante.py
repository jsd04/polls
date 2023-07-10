# Generated by Django 4.2.2 on 2023-07-10 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioInquilo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('curp', models.CharField(max_length=30)),
                ('piso', models.IntegerField()),
                ('departamento', models.IntegerField()),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=30)),
                ('creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioVisitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('curp', models.CharField(max_length=30)),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nombre_inquilino', models.CharField(max_length=30)),
                ('parentesco', models.CharField(max_length=30)),
            ],
        ),
    ]