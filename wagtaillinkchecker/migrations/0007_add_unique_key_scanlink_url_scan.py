from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaillinkchecker', '0006_increase_url_maxlength'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scanlink',
            unique_together=set([('url', 'scan')]),
        ),
    ]