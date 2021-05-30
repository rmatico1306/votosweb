# Generated by Django 3.2.3 on 2021-05-17 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seccion', models.CharField(max_length=6)),
                ('tipo_casilla', models.CharField(max_length=30)),
                ('num_votoChelo', models.IntegerField(verbose_name='INDEPENDIENTE, JESUS ABRAHAM CANO GONZALEZ')),
                ('num_votoMorena', models.IntegerField(verbose_name='MORENA, OSCAR ENRIQUE RAMOS MENDEZ')),
                ('num_prd', models.IntegerField(verbose_name='PRD, HOMERO YAÑEZ RUIZ')),
                ('num_pri', models.IntegerField(verbose_name='PRI/PAN(COALICIO), AURORA PIÑERA FERNANDEZ')),
                ('num_pt', models.IntegerField(verbose_name='PT, JOAQUIN ANTONIO SOLIS MENDOZA')),
                ('num_verde', models.IntegerField(verbose_name='PARTIDO VERDE ECOLOGISTA,JUANA DEL CARMEN LOPEZ GRANIER')),
                ('num_movimientociudadano', models.IntegerField(verbose_name='MOVIMIENTO CIUDADANO, PATRICIA ELEJO ALMEIDA')),
                ('num_encuentrosolidario', models.IntegerField(verbose_name='PARTIDO ENCUENTRO SOLIDARIO')),
                ('num_redesSociales', models.IntegerField(verbose_name='REDES SOCIALES PROGRECISTAS, FRANCISCO PEREZ PONSE')),
                ('num_fuerzaMexico', models.IntegerField(verbose_name='FUERZA POR MEXICO, MARIA LUZ GALLEGO VAZQUEZ')),
                ('num_candidatosNoRegistrados', models.IntegerField(verbose_name='CANDIDATOS NO REGISTRADOS')),
                ('num_votoNulos', models.IntegerField(verbose_name='VOTOS NULOS')),
                ('total_votos', models.IntegerField(verbose_name='TOTAL DE VOTOS')),
            ],
        ),
        migrations.CreateModel(
            name='Politico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('partidoPolitico', models.CharField(max_length=30)),
                ('correo', models.EmailField(blank=True, max_length=254)),
                ('fecha', models.DateField(null=True)),
            ],
        ),
    ]