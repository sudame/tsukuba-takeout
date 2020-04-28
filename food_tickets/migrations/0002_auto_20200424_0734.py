# Generated by Django 3.0.5 on 2020-04-24 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='food_tickets.Store'),
        ),
    ]