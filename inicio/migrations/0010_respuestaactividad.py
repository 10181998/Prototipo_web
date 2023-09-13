# Generated by Django 3.2.19 on 2023-09-17 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0009_activity_vr_cards'),
    ]

    operations = [
        migrations.CreateModel(
            name='RespuestaActividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo_respuesta', models.FileField(upload_to='respuestas/')),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.activity')),
            ],
        ),
    ]
