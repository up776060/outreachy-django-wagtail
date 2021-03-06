# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-25 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_auto_20180125_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantapproval',
            name='contractor',
            field=models.BooleanField(help_text='Will you be a contractor during the Outreachy internship period?'),
        ),
        migrations.AlterField(
            model_name='applicantapproval',
            name='eligible_to_work',
            field=models.BooleanField(help_text='Are you eligible to work for 40 hours a week in the country you will be living in during the Outreachy internship period?<br>Please note that in some countries, students studying abroad on a student visa may not be eligible to work full-time (40 hours a week). If you are on a student visa, please double check with your school counselors before applying.<br>Additionally, in some countries, spousal visas may not allow spouses to work. Please contact your immigration officer if you have any questions about whether your visa will be impacted by full-time work (40 hours a week).'),
        ),
        migrations.AlterField(
            model_name='applicantapproval',
            name='employed',
            field=models.BooleanField(help_text='Will you be a part-time or full-time employee during the Outreachy internship period?'),
        ),
        migrations.AlterField(
            model_name='applicantapproval',
            name='enrolled_as_student',
            field=models.BooleanField(help_text='Will you be enrolled in a university or college during the Outreachy internship period?'),
        ),
        migrations.AlterField(
            model_name='applicantapproval',
            name='gsoc_or_outreachy_internship',
            field=models.BooleanField(help_text='Have you been accepted as a Google Summer of Code intern or an Outreachy intern before? Please say yes even if you did not complete the internship.'),
        ),
        migrations.AlterField(
            model_name='applicantapproval',
            name='living_in_us',
            field=models.BooleanField(help_text='Will you be living in the United States of America during the Outreachy internship period? Please answer yes if you are living in the USA, even if you are a citizen of a country other than USA.'),
        ),
        migrations.AlterField(
            model_name='applicantapproval',
            name='over_18',
            field=models.BooleanField(help_text='Will you be 18 years or older when the Outreachy internship period starts?'),
        ),
        migrations.AlterField(
            model_name='applicantapproval',
            name='time_commitments',
            field=models.BooleanField(help_text='Will you have other time commitments that require more than 10 hours a week during the Outreachy internship period?'),
        ),
        migrations.AlterField(
            model_name='applicantapproval',
            name='under_export_control',
            field=models.BooleanField(help_text='Are you a person or entity restricted by US export controls or sanctions programs?'),
        ),
        migrations.AlterField(
            model_name='applicantapproval',
            name='us_national_or_permanent_resident',
            field=models.BooleanField(help_text='Are you a national or permanent resident of the United States of America?'),
        ),
        migrations.AlterField(
            model_name='applicantapproval',
            name='us_resident_demographics',
            field=models.BooleanField(help_text='Are you Black/African American, Hispanic/Latin@, Native American, Alaska Native, Native Hawaiian, or Pacific Islander?'),
        ),
        migrations.AlterField(
            model_name='applicantapproval',
            name='us_sanctioned_country',
            field=models.BooleanField(help_text='Are you a resident or national of Crimea, Cuba, Iran, North Korea, or Syria? If you have citizenship with of one of these counties, please answer yes, even if you are not currently living in those countries.'),
        ),
    ]
