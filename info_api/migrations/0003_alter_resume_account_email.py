# Generated by Django 4.0 on 2022-06-15 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info_api', '0002_professional_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='account_email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='info_api.account'),
        ),
    ]