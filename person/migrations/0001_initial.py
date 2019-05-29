# Generated by Django 2.0.7 on 2019-03-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutGuitar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('overview', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='guitar')),
            ],
        ),
        migrations.CreateModel(
            name='Batches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=60)),
                ('batch_datetime', models.DateTimeField()),
                ('days', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=15)),
                ('details', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Buyguitar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('amount', models.CharField(max_length=60)),
                ('details', models.CharField(max_length=60)),
                ('overview', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='guitar')),
            ],
        ),
        migrations.CreateModel(
            name='Feestructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Programmes_name', models.CharField(max_length=50)),
                ('Days_per_week', models.CharField(max_length=50)),
                ('Class_duration', models.CharField(max_length=50)),
                ('fees', models.CharField(max_length=50)),
                ('certification', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeVideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('link', models.CharField(max_length=300)),
            ],
        ),
    ]
