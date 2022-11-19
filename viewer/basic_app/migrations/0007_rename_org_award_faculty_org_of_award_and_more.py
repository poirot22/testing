# Generated by Django 4.0.3 on 2022-11-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0006_faculty_article_title_faculty_award_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='org_award',
            new_name='org_of_award',
        ),
        migrations.RenameField(
            model_name='faculty',
            old_name='permanentAddressSameAsCurrentAddress',
            new_name='permanent_address_is_same_as_current_address',
        ),
        migrations.RenameField(
            model_name='faculty',
            old_name='year_award',
            new_name='year_of_award',
        ),
        migrations.AlterField(
            model_name='faculty',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+ve', 'A+ve'), ('B+ve', 'B+ve'), ('A-ve', 'A-ve'), ('B-ve', 'B-ve'), ('O+ve', 'O+ve'), ('AB-ve', 'AB-ve')], max_length=5),
        ),
    ]
