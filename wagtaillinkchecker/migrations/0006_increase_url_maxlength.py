from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaillinkchecker', '0005_auto_20180922_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scanlink',
            name='url',
            field=models.URLField(max_length=2048),
        ),
    ]
