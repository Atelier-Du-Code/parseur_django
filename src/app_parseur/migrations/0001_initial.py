# Generated by Django 5.1.6 on 2025-03-02 10:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_produit', models.CharField(max_length=255)),
                ('editeur', models.CharField(max_length=255)),
                ('version_produit', models.CharField(blank=True, max_length=100, null=True)),
                ('niveau_eal', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('document', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_upload.document')),
            ],
        ),
    ]
