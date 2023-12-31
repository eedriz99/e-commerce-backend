# Generated by Django 5.0 on 2023-12-21 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orderId',
            new_name='orderID',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='userId',
            new_name='userID',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='orderStatus',
            field=models.CharField(choices=[('Submitted', 'Submitted'), ('Processed', 'Processed')], max_length=10, null=True),
        ),
    ]
