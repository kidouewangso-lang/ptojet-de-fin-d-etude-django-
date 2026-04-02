import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings')
django.setup()

from django.contrib.auth import get_user_model
from faculty.models import Department, Teacher, Subject, Holiday, TimeTable, Exam, ExamResult
from student.models import Parent, Student
from datetime import date, time

User = get_user_model()

print("=== Peuplement de la base de données PreSkool ===\n")
print("🧹 Nettoyage des anciennes données de test...")
ExamResult.objects.all().delete()
Exam.objects.all().delete()
TimeTable.objects.all().delete()
Holiday.objects.all().delete()
Subject.objects.all().delete()
Teacher.objects.all().delete()
Student.objects.all().delete()
Parent.objects.all().delete()
Department.objects.all().delete()
# Supprimer les utilisateurs de test (pas l'admin)
User.objects.filter(username__startswith='prof_').delete()
print("   ✅ Nettoyage terminé.\n")

# --- 1. Départements ---
print("📁 Création des départements...")
dept_info = Department.objects.create(name='Informatique', head_of_department='Dr. Karim Benali', started_date=date(2020, 9, 1), student_capacity=120)
dept_math = Department.objects.create(name='Mathématiques', head_of_department='Pr. Fatima Zahra', started_date=date(2019, 9, 1), student_capacity=100)
dept_sci = Department.objects.create(name='Sciences Physiques', head_of_department='Dr. Youssef Alami', started_date=date(2018, 9, 1), student_capacity=80)
print(f"   ✅ {Department.objects.count()} départements créés.")

# --- 2. Professeurs ---
print("\n👨‍🏫 Création des professeurs...")

teacher_data = [
    {'username': 'prof_benali', 'first_name': 'Karim', 'last_name': 'Benali', 'email': 'k.benali@preskool.ma', 'teacher_id': 'T001', 'gender': 'Male', 'dob': date(1980, 3, 15), 'mobile': '0661234567', 'joining': date(2020, 9, 1), 'qualification': 'Doctorat Informatique', 'experience': '12 ans', 'dept': dept_info},
    {'username': 'prof_zahra', 'first_name': 'Fatima', 'last_name': 'Zahra', 'email': 'f.zahra@preskool.ma', 'teacher_id': 'T002', 'gender': 'Female', 'dob': date(1985, 7, 22), 'mobile': '0667654321', 'joining': date(2019, 9, 1), 'qualification': 'Agrégation Mathématiques', 'experience': '8 ans', 'dept': dept_math},
    {'username': 'prof_alami', 'first_name': 'Youssef', 'last_name': 'Alami', 'email': 'y.alami@preskool.ma', 'teacher_id': 'T003', 'gender': 'Male', 'dob': date(1978, 11, 5), 'mobile': '0669876543', 'joining': date(2018, 9, 1), 'qualification': 'Doctorat Physique', 'experience': '15 ans', 'dept': dept_sci},
]

teachers = {}
for td in teacher_data:
    user = User.objects.create_user(
        username=td['username'], password='preskool2026',
        first_name=td['first_name'], last_name=td['last_name'], email=td['email'],
        role='teacher', is_teacher=True, is_student=False
    )
    teacher = Teacher.objects.create(
        user=user, teacher_id=td['teacher_id'], gender=td['gender'], date_of_birth=td['dob'],
        mobile_number=td['mobile'], joining_date=td['joining'], qualification=td['qualification'],
        experience=td['experience'], address='Casablanca, Maroc', department=td['dept']
    )
    teachers[td['teacher_id']] = teacher

print(f"   ✅ {Teacher.objects.count()} professeurs créés.")

# --- 3. Matières ---
print("\n📚 Création des matières...")

subjects_data = [
    {'subject_id': 'INF101', 'name': 'Python & Django', 'dept': dept_info, 'teacher': teachers['T001']},
    {'subject_id': 'INF102', 'name': 'Algorithmique', 'dept': dept_info, 'teacher': teachers['T001']},
    {'subject_id': 'MAT201', 'name': 'Analyse Mathématique', 'dept': dept_math, 'teacher': teachers['T002']},
    {'subject_id': 'MAT202', 'name': 'Algèbre Linéaire', 'dept': dept_math, 'teacher': teachers['T002']},
    {'subject_id': 'PHY301', 'name': 'Mécanique Générale', 'dept': dept_sci, 'teacher': teachers['T003']},
    {'subject_id': 'PHY302', 'name': 'Thermodynamique', 'dept': dept_sci, 'teacher': teachers['T003']},
]

subjects = {}
for sd in subjects_data:
    subj = Subject.objects.create(subject_id=sd['subject_id'], name=sd['name'], department=sd['dept'], teacher=sd['teacher'])
    subjects[sd['subject_id']] = subj

print(f"   ✅ {Subject.objects.count()} matières créées.")

# --- 4. Étudiants & Parents ---
print("\n🎓 Création des étudiants et de leurs parents...")

students_data = [
    {'first': 'Omar', 'last': 'El Fassi', 'sid': 'STU001', 'gender': 'Male', 'dob': date(2005, 4, 12), 'cls': '2ème Année', 'joining': date(2023, 9, 5), 'mobile': '0612345678', 'admission': 'ADM001', 'section': 'A', 'father': 'Hassan El Fassi', 'f_occ': 'Ingénieur', 'f_mobile': '0661112233', 'f_email': 'h.elfassi@mail.com', 'mother': 'Amina El Fassi', 'm_occ': 'Médecin', 'm_mobile': '0662223344', 'm_email': 'a.elfassi@mail.com'},
    {'first': 'Sara', 'last': 'Bennani', 'sid': 'STU002', 'gender': 'Female', 'dob': date(2004, 8, 25), 'cls': '3ème Année', 'joining': date(2022, 9, 3), 'mobile': '0623456789', 'admission': 'ADM002', 'section': 'B', 'father': 'Rachid Bennani', 'f_occ': 'Avocat', 'f_mobile': '0663334455', 'f_email': 'r.bennani@mail.com', 'mother': 'Khadija Bennani', 'm_occ': 'Professeur', 'm_mobile': '0664445566', 'm_email': 'k.bennani@mail.com'},
    {'first': 'Yassine', 'last': 'Tazi', 'sid': 'STU003', 'gender': 'Male', 'dob': date(2005, 1, 30), 'cls': '2ème Année', 'joining': date(2023, 9, 5), 'mobile': '0634567890', 'admission': 'ADM003', 'section': 'A', 'father': 'Mohammed Tazi', 'f_occ': 'Commerçant', 'f_mobile': '0665556677', 'f_email': 'm.tazi@mail.com', 'mother': 'Laila Tazi', 'm_occ': 'Pharmacienne', 'm_mobile': '0666667788', 'm_email': 'l.tazi@mail.com'},
    {'first': 'Nadia', 'last': 'Chraibi', 'sid': 'STU004', 'gender': 'Female', 'dob': date(2004, 11, 8), 'cls': '3ème Année', 'joining': date(2022, 9, 3), 'mobile': '0645678901', 'admission': 'ADM004', 'section': 'B', 'father': 'Abdelkader Chraibi', 'f_occ': 'Architecte', 'f_mobile': '0667778899', 'f_email': 'a.chraibi@mail.com', 'mother': 'Houda Chraibi', 'm_occ': 'Enseignante', 'm_mobile': '0668889900', 'm_email': 'h.chraibi@mail.com'},
    {'first': 'Amine', 'last': 'Kettani', 'sid': 'STU005', 'gender': 'Male', 'dob': date(2006, 2, 14), 'cls': '1ère Année', 'joining': date(2024, 9, 2), 'mobile': '0656789012', 'admission': 'ADM005', 'section': 'A', 'father': 'Tarik Kettani', 'f_occ': 'Directeur Bancaire', 'f_mobile': '0669990011', 'f_email': 't.kettani@mail.com', 'mother': 'Salma Kettani', 'm_occ': 'Journaliste', 'm_mobile': '0660001122', 'm_email': 's.kettani@mail.com'},
]

for sd in students_data:
    parent = Parent.objects.create(
        father_name=sd['father'], father_occupation=sd['f_occ'], father_mobile=sd['f_mobile'], father_email=sd['f_email'],
        mother_name=sd['mother'], mother_occupation=sd['m_occ'], mother_mobile=sd['m_mobile'], mother_email=sd['m_email'],
        present_address='Casablanca, Maroc', permanent_address='Casablanca, Maroc'
    )
    Student.objects.create(
        first_name=sd['first'], last_name=sd['last'], student_id=sd['sid'], gender=sd['gender'],
        date_of_birth=sd['dob'], student_class=sd['cls'], joining_date=sd['joining'],
        mobile_number=sd['mobile'], admission_number=sd['admission'], section=sd['section'], parent=parent
    )

print(f"   ✅ {Student.objects.count()} étudiants créés.")

# --- 5. Vacances ---
print("\n🏖️  Création des périodes de vacances...")
Holiday.objects.create(name='Vacances de Printemps', start_date=date(2026, 4, 5), end_date=date(2026, 4, 20), description='Pause de printemps du semestre 2.')
Holiday.objects.create(name='Aïd Al Fitr', start_date=date(2026, 3, 30), end_date=date(2026, 4, 2), description='Célébration de la fin du Ramadan.')
Holiday.objects.create(name='Fête du Trône', start_date=date(2026, 7, 30), end_date=date(2026, 7, 31), description='Fête nationale du Maroc.')
print(f"   ✅ {Holiday.objects.count()} périodes de vacances créées.")

# --- 6. Examens ---
print("\n📝 Création des examens...")
Exam.objects.create(name='Examen Final Python', subject=subjects['INF101'], date=date(2026, 6, 15), start_time=time(9, 0), end_time=time(11, 0), room_no='Salle A1')
Exam.objects.create(name='Examen Final Algorithmique', subject=subjects['INF102'], date=date(2026, 6, 17), start_time=time(14, 0), end_time=time(16, 0), room_no='Salle A2')
Exam.objects.create(name='Partiel Analyse', subject=subjects['MAT201'], date=date(2026, 5, 20), start_time=time(10, 0), end_time=time(12, 0), room_no='Salle B1')
Exam.objects.create(name='Contrôle Mécanique', subject=subjects['PHY301'], date=date(2026, 5, 25), start_time=time(8, 0), end_time=time(10, 0), room_no='Labo P1')
print(f"   ✅ {Exam.objects.count()} examens créés.")

# --- 7. Emploi du temps ---
print("\n📅 Création de l'emploi du temps...")
TimeTable.objects.create(department=dept_info, subject=subjects['INF101'], teacher=teachers['T001'], day_of_week='Monday', start_time=time(9, 0), end_time=time(11, 0), room_no='Salle Info 1')
TimeTable.objects.create(department=dept_info, subject=subjects['INF102'], teacher=teachers['T001'], day_of_week='Wednesday', start_time=time(14, 0), end_time=time(16, 0), room_no='Salle Info 2')
TimeTable.objects.create(department=dept_math, subject=subjects['MAT201'], teacher=teachers['T002'], day_of_week='Tuesday', start_time=time(10, 0), end_time=time(12, 0), room_no='Salle Math 1')
TimeTable.objects.create(department=dept_sci, subject=subjects['PHY301'], teacher=teachers['T003'], day_of_week='Thursday', start_time=time(8, 0), end_time=time(10, 0), room_no='Labo Physique')
print(f"   ✅ {TimeTable.objects.count()} créneaux d'emploi du temps créés.")

# --- Résumé Final ---
print("\n" + "=" * 50)
print("🎉 BASE DE DONNÉES PEUPLÉE AVEC SUCCÈS !")
print("=" * 50)
print(f"   📁 Départements : {Department.objects.count()}")
print(f"   👨‍🏫 Professeurs  : {Teacher.objects.count()}")
print(f"   📚 Matières     : {Subject.objects.count()}")
print(f"   🎓 Étudiants    : {Student.objects.count()}")
print(f"   📝 Examens      : {Exam.objects.count()}")
print(f"   📅 Emploi tps   : {TimeTable.objects.count()}")
print(f"   🏖️  Vacances     : {Holiday.objects.count()}")
print("=" * 50)
