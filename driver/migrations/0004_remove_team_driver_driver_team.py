# Generated by Django 4.2.3 on 2023-07-28 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='driver',
        ),
        migrations.AddField(
            model_name='driver',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='driver.team'),
            preserve_default=False,
        ),
    ]
