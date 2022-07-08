# Generated by Django 4.0.5 on 2022-06-09 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('participacoes', '0002_participante_estadocivil_remove_retiro_participantes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retiro',
            name='participantes',
        ),
        migrations.CreateModel(
            name='Participacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participacoes.participante')),
                ('retiro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='participacoes.retiro')),
            ],
            options={
                'verbose_name': 'Participacao',
                'verbose_name_plural': 'Participacoes',
                'db_table': 'participacao',
            },
        ),
    ]