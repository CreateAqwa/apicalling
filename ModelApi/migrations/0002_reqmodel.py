# Generated by Django 5.0.2 on 2024-04-03 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReqModel',
            fields=[
                ('name', models.AutoField(primary_key=True, serialize=False)),
                ('continu', models.CharField(max_length=50)),
                ('loca', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('Mone', 'Mone'), ('Light', 'Light'), ('Black', 'Black')], max_length=100)),
                ('added_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
