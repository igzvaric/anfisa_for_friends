# Generated by Django 3.2.16 on 2024-07-21 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0003_auto_20240721_1021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='icecream',
            options={'ordering': ('output_order', 'title'), 'verbose_name': 'Мороженое', 'verbose_name_plural': 'Мороженое'},
        ),
        migrations.RenameField(
            model_name='icecream',
            old_name='output_otder',
            new_name='output_order',
        ),
    ]
