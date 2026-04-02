import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings')
django.setup()
from django.contrib.auth import get_user_model

User = get_user_model()

# 1. Admin
if not User.objects.filter(username='admin_demo').exists():
    User.objects.create_superuser('admin_demo', 'admin@preskool.com', 'admin1234')

# 2. Enseignant
if not User.objects.filter(username='prof_demo').exists():
    user_prof = User.objects.create_user(username='prof_demo', password='password123', role='teacher', is_teacher=True)

# 3. Etudiant
if not User.objects.filter(username='student_demo').exists():
    user_etu = User.objects.create_user(username='student_demo', password='password123', role='student', is_student=True)

print("Comptes de démo créés avec succès !")
