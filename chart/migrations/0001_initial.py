# Generated by Django 4.0.4 on 2022-09-10 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('data', models.CharField(max_length=100000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('target', models.SmallIntegerField()),
                ('source', models.SmallIntegerField()),
                ('data', models.CharField(max_length=100000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
