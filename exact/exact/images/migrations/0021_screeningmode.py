# Generated by Django 2.0.13 on 2019-12-31 13:04

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0020_auto_20191209_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScreeningMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screening_tiles', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('x_steps', models.IntegerField(default=0)),
                ('y_steps', models.IntegerField(default=0)),
                ('current_index', models.IntegerField(default=0)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screening', to='images.Image')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
