# Generated by Django 5.1.7 on 2025-05-06 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0002_alter_kernelcompilation_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kernelcompilation',
            name='variant',
            field=models.CharField(choices=[('def', 'Debug'), ('perf', 'Performance')], default='def', max_length=255),
        ),
    ]
