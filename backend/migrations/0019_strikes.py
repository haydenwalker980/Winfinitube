# Generated by Django 3.0.7 on 2021-02-17 00:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoStrike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.CharField(choices=[('CY', 'Copyright'), ('CG', 'Community Guidelines')], max_length=2)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Channel')),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Video')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentStrike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.CharField(choices=[('CY', 'Copyright'), ('CG', 'Community Guidelines')], max_length=2)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Channel')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Comment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]