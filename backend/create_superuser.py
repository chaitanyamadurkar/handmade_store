import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'handmade_store.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='madurkarc34@gmail.com',
        password='Chai@1234'
    )
    print('Superuser created!')
else:
    print('Superuser already exists.')
