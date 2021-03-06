# Generated by Django 3.0.7 on 2021-01-10 00:42

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_channelbackground_desktop_image_repeat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channelbackground',
            name='color',
            field=colorfield.fields.ColorField(blank=True, default='#CCCCCC', max_length=18),
        ),
        migrations.AlterField(
            model_name='channelbackground',
            name='desktop_image_repeat',
            field=models.CharField(blank=True, choices=[('NR', 'no-repeat'), ('RE', 'repeat'), ('RX', 'repeat-x'), ('RY', 'repeat-y')], default='NR', max_length=2),
        ),
        migrations.CreateModel(
            name='WatchHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch_history', to='backend.Channel')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='backend.Video')),
            ],
        ),
    ]
