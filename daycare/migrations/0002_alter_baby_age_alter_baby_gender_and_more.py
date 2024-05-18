# Generated by Django 5.0.6 on 2024-05-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daycare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baby',
            name='age',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='baby',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=10),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='sitter_number',
            field=models.CharField(max_length=8, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='amount_UGX',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity_bought',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity_in_stock',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity_issued_out',
            field=models.IntegerField(default=''),
        ),
    ]
