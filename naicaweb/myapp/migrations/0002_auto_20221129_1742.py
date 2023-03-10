# Generated by Django 3.2 on 2022-11-29 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ally',
            options={'verbose_name_plural': 'allies'},
        ),
        migrations.AddField(
            model_name='ally',
            name='ally_industry',
            field=models.CharField(choices=[('1', 'Real State'), ('2', 'Software'), ('3', 'Construction'), ('4', 'Trading Goods')], default='1', max_length=2),
        ),
        migrations.AddField(
            model_name='ally',
            name='ally_url',
            field=models.URLField(blank=True, db_index=True, max_length=250, unique=True),
        ),
    ]
