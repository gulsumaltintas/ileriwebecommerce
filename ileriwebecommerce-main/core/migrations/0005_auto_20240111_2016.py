# Generated by Django 2.2.14 on 2024-01-11 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoriTitle', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Polo tisort'), ('OW', 'Outwear')], max_length=2),
        ),
    ]
