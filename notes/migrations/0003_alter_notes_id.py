# Generated by Django 5.0.4 on 2024-04-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_remove_notes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
