# Generated by Django 3.0.6 on 2020-05-15 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('asunto', models.CharField(max_length=30)),
                ('comentario', models.TextField()),
            ],
        ),
    ]
