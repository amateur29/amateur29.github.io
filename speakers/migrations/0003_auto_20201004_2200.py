# Generated by Django 2.2.6 on 2020-10-04 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0002_auto_20200908_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speaker',
            old_name='comment',
            new_name='know_speaker_description',
        ),
        migrations.RenameField(
            model_name='speaker',
            old_name='name',
            new_name='nominator_name',
        ),
        migrations.AddField(
            model_name='speaker',
            name='nominee_about',
            field=models.TextField(default='N/A'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='nominee_name',
            field=models.CharField(default='N/A', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='social_links',
            field=models.TextField(default='N/A'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='spoken_publicly_links',
            field=models.TextField(default='N/A'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='talk_about',
            field=models.TextField(default='N/A'),
            preserve_default=False,
        ),
    ]
