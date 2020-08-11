# Generated by Django 3.0.7 on 2020-08-02 14:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20200802_1148'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificate',
            options={'ordering': ('-completed',)},
        ),
        migrations.AddField(
            model_name='certificate',
            name='completed',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]