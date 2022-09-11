from django.db import migrations
from django.contrib.auth.models import User


def create_user(apps, schema_editor):
    user1 = User.objects.create(
        username='hr',
        email='hr@gmail.com',
        password='adminadmin',
        is_superuser=False,
        is_staff=False
    )
    user1.set_password('adminadmin')
    user1.save()
    user2 = User.objects.create(
        username='qa',
        email='qa@gmail.com',
        password='adminadmin',
        is_superuser=False,
        is_staff=False
    )
    user2.set_password('adminadmin')
    user2.save()
    user3 = User.objects.create(
        username='manager',
        email='manager@gmail.com',
        password='adminadmin',
        is_superuser=False,
        is_staff=True
    )
    user3.set_password('adminadmin')
    user3.save()
    user4 = User.objects.create(
        username='jamie@amazon.com',
        email='jamie@amazon.com',
        first_name='Jamie',
        password='adminadmin',
        is_superuser=False,
        is_staff=True
    )
    user4.set_password('adminadmin')
    user4.save()


class Migration(migrations.Migration):
    operations = [
        migrations.RunPython(create_user),
    ]
