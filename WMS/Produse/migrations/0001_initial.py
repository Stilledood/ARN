# Generated by Django 4.2.4 on 2023-08-10 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Depozit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=250)),
                ('tara_de_origine', models.CharField(max_length=200)),
                ('persoana_contact', models.CharField(blank=True, max_length=100)),
                ('telefon_persoana_contact', models.CharField(blank=True, max_length=30)),
                ('email_persoana_contact', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'ordering': ['nume'],
            },
        ),
        migrations.CreateModel(
            name='Produs',
            fields=[
                ('cod_produs', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nume', models.CharField(max_length=200)),
                ('inaltime', models.IntegerField()),
                ('latime', models.IntegerField()),
                ('lungime', models.IntegerField()),
                ('producator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Produse.producator')),
            ],
            options={
                'ordering': ['nume'],
            },
        ),
        migrations.CreateModel(
            name='ProductSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantitate', models.IntegerField()),
                ('produs', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Produse.produs')),
                ('raft', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Depozit.raft')),
            ],
        ),
    ]
