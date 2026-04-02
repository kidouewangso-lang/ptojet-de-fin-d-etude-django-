import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings')
django.setup()
from django.contrib.auth.models import Group

groups = ['Administration', 'Enseignants', 'Étudiants', 'Parents']
for group_name in groups:
    group, created = Group.objects.get_or_create(name=group_name)
    if created:
        print(f"Groupe '{group_name}' créé avec succès.")
    else:
        print(f"Groupe '{group_name}' existait déjà.")
print("Opération terminée.")
