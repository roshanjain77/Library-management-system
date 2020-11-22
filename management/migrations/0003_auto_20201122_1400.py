# Generated by Django 3.0.9 on 2020-11-22 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0002_auto_20201122_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower',
            name='fine',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='tot_fine',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='borrower',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed', to=settings.AUTH_USER_MODEL),
        ),
    ]
