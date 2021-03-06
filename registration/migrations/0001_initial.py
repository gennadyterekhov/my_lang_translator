# Generated by Django 2.2.12 on 2020-04-24 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Conlang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.User')),
            ],
        ),
    ]
