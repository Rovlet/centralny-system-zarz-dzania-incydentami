# Generated by Django 3.0.6 on 2020-06-04 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200604_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sciezkapytan',
            name='id_next_pytanie_jesli_nie',
            field=models.ForeignKey(blank=True, db_column='id_next_pytanie_jesli_nie', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='id_next_pytanie_jesli_nie', to='user.Pytanie'),
        ),
        migrations.AlterField(
            model_name='sciezkapytan',
            name='id_next_pytanie_jesli_tak',
            field=models.ForeignKey(blank=True, db_column='id_next_pytanie_jesli_tak', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='id_next_pytanie_jesli_tak', to='user.Pytanie'),
        ),
    ]
