from django.shortcuts import render
from django.views.generic import View
from .models import *


def menu(request):
    return render(request, 'menu.html')


class SchoolView(View):
    def get(self, request):
        schools = School.objects.all()
        context = {
            'title': "School modeli",
            'schools': schools
        }
        return render(request, 'school.html', context)

    def post(self, request):
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')

        schools = School.objects.all()
        context = {
            'title': "School modeli",
            'schools': schools
        }

        if name and address and phone_number:
            School.objects.create(
                name=name,
                address=address,
                phone_number=phone_number
            )
            context['message'] = f"{name} qo'shildi"
        else:
            context['message'] = "Qo'shilmadi. Ma'lumotlar to'liq emas!"

        return render(request, 'school.html', context)


class TeacherView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        schools = School.objects.all()
        context = {
            'title': "Teacher modeli",
            'teachers': teachers,
            'schools': schools
        }
        return render(request, 'teacher.html', context)

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        school_id = request.POST.get('school')
        school = School.objects.get(id=school_id)

        teachers = Teacher.objects.all()
        schools = School.objects.all()
        context = {
            'title': "Teacher modeli",
            'teachers': teachers,
            'schools': schools
        }

        if first_name and last_name and email and phone_number and school:
            Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                school=school
            )
            context['message'] = f"{first_name} {last_name} qo'shildi"
        else:
            context['message'] = "Qo'shilmadi. Ma'lumotlar to'liq emas!"

        return render(request, 'teacher.html', context)


class StudentView(View):
    def get(self, request):
        students = Student.objects.all()
        schools = School.objects.all()

        context = {
            'title': "Student modeli",
            'students': students,
            'schools': schools
        }
        return render(request, 'student.html', context)

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        school_id = request.POST.get('school')
        school = School.objects.get(id=school_id)

        students = Student.objects.all()
        schools = School.objects.all()
        context = {
            'title': "Teacher modeli",
            'students': students,
            'schools': schools
        }

        if first_name and last_name and date_of_birth and gender and school:
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                gender=gender,
                school=school
            )
            context['message'] = f"{first_name} {last_name} qo'shildi"
        else:
            context['message'] = "Qo'shilmadi. Ma'lumotlar to'liq emas!"

        return render(request, 'student.html', context)


class ClassView(View):
    def get(self, request):
        classes = Class.objects.all()
        teachers = Teacher.objects.all()
        schools = School.objects.all()

        context = {
            'title': "Class modeli",
            'classes': classes,
            'teachers': teachers,
            'schools': schools
        }
        return render(request, 'class.html', context)

    def post(self, request):
        name = request.POST.get('name')
        teacher_id = request.POST.get('teacher')
        school_id = request.POST.get('school')

        teacher = Teacher.objects.get(id=teacher_id)
        school = School.objects.get(id=school_id)

        classes = Class.objects.all()
        teachers = Teacher.objects.all()
        schools = School.objects.all()
        context = {
            'title': "Class modeli",
            'classes': classes,
            'teachers': teachers,
            'schools': schools
        }

        if name and teacher and school:
            Class.objects.create(
                name=name,
                teacher=teacher,
                school=school
            )
            context['message'] = f"{name} sinfi qo'shildi"
        else:
            context['message'] = "Qo'shilmadi. Ma'lumotlar to'liq emas!"

        return render(request, 'class.html', context)


class SubjectView(View):
    def get(self, request):
        subjects = Subject.objects.all()
        classes = Class.objects.all()
        teachers = Teacher.objects.all()

        context = {
            'title': "Subject modeli",
            'subjects': subjects,
            'classes': classes,
            'teachers': teachers
        }
        return render(request, 'subject.html', context)

    def post(self, request):
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        teacher_id = request.POST.get('teacher')

        class_obj = Class.objects.get(id=class_id)
        teacher = Teacher.objects.get(id=teacher_id)

        subjects = Subject.objects.all()
        classes = Class.objects.all()
        teachers = Teacher.objects.all()
        context = {
            'title': "Subject modeli",
            'subjects': subjects,
            'classes': classes,
            'teachers': teachers
        }

        if name and class_obj and teacher:
            Subject.objects.create(
                name=name,
                class_id=class_obj,
                teacher=teacher
            )
            context['message'] = f"{name} fani qo'shildi"
        else:
            context['message'] = "Qo'shilmadi. Ma'lumotlar to'liq emas!"

        return render(request, 'subject.html', context)


class EnrollmentView(View):
    def get(self, request):
        enrollments = Enrollment.objects.all()
        students = Student.objects.all()
        classes = Class.objects.all()

        context = {
            'title': "O'quvchilarni sinfga joylashtirish",
            'enrollments': enrollments,
            'students': students,
            'classes': classes
        }
        return render(request, 'enrollment.html', context)

    def post(self, request):
        student_id = request.POST.get('student')
        class_id = request.POST.get('class_id')

        student = Student.objects.get(id=student_id)
        class_obj = Class.objects.get(id=class_id)

        enrollments = Enrollment.objects.all()
        students = Student.objects.all()
        classes = Class.objects.all()
        context = {
            'title': "O'quvchilarni sinfga joylashtirish",
            'enrollments': enrollments,
            'students': students,
            'classes': classes
        }

        if student and class_obj:
            Enrollment.objects.create(
                student=student,
                class_id=class_obj
            )
            context['message'] = f"{student} {class_obj} sinfiga joylashtirildi"
        else:
            context['message'] = "Joylashtirish muvaffaqiyatsiz bo'ldi. Ma'lumotlar to'liq emas!"

        return render(request, 'enrollment.html', context)


class GradeView(View):
    def get(self, request):
        grades = Grade.objects.all()
        students = Student.objects.all()
        subjects = Subject.objects.all()

        context = {
            'title': "Baholar",
            'grades': grades,
            'students': students,
            'subjects': subjects
        }
        return render(request, 'grade.html', context)

    def post(self, request):
        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')
        grade_value = request.POST.get('grade_value')

        student = Student.objects.get(id=student_id)
        subject = Subject.objects.get(id=subject_id)

        grades = Grade.objects.all()
        students = Student.objects.all()
        subjects = Subject.objects.all()
        context = {
            'title': "Baholar",
            'grades': grades,
            'students': students,
            'subjects': subjects
        }

        if student and subject and grade_value:
            Grade.objects.create(
                student=student,
                subject=subject,
                grade_value=grade_value
            )
            context['message'] = f"{student} uchun {subject} fanidan {grade_value} qo'yildi"
        else:
            context['message'] = "Baho qo'yilmadi. Ma'lumotlar to'liq emas!"

        return render(request, 'grade.html', context)


class AttendanceView(View):
    def get(self, request):
        attendances = Attendance.objects.all()
        students = Student.objects.all()
        classes = Class.objects.all()

        context = {
            'title': "Davomat",
            'attendances': attendances,
            'students': students,
            'classes': classes
        }
        return render(request, 'attendance.html', context)

    def post(self, request):
        student_id = request.POST.get('student')
        class_id = request.POST.get('class')
        student = Student.objects.get(id=student_id)
        class_obj = Class.objects.get(id=class_id)

        attendances = Attendance.objects.all()
        students = Student.objects.all()
        classes = Class.objects.all()
        context = {
            'title': "Davomat",
            'attendances': attendances,
            'students': students,
            'classes': classes
        }

        if student and class_obj:
            Attendance.objects.create(
                student=student,
                class_id=class_obj
            )
            context['message'] = f"{student} uchun {class_obj.name} sinfiga davomat belgilandi"
        else:
            context['message'] = "Davomat belgilanmadi. Ma'lumotlar to'liq emas!"

        return render(request, 'attendance.html', context)


# Qo'shimcha vazifalar
class ParentGuardianView(View):
    def get(self, request):
        guardians = ParentGuardian.objects.all()
        students = Student.objects.all()

        context = {
            'title': "Ota-ona yoki Vasiy",
            'guardians': guardians,
            'students': students
        }
        return render(request, 'parent_guardian.html', context)

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        relationship = request.POST.get('relationship')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        student_id = request.POST.get('student')
        student = Student.objects.get(id=student_id)

        guardians = ParentGuardian.objects.all()
        students = Student.objects.all()
        context = {
            'title': "Ota-ona yoki Vasiy",
            'guardians': guardians,
            'students': students
        }

        if first_name and last_name and relationship and phone_number and email and student:
            ParentGuardian.objects.create(
                first_name=first_name,
                last_name=last_name,
                relationship=relationship,
                phone_number=phone_number,
                email=email,
                student=student
            )
            context['message'] = f"{first_name} {last_name} ({relationship}) qo'shildi"
        else:
            context['message'] = "Ma'lumotlar to'liq emas, iltimos, to'ldiring!"

        return render(request, 'parent_guardian.html', context)


class CourseView(View):
    def get(self, request):
        courses = Course.objects.all()
        context = {
            'title': "Kurslar ro'yxati",
            'courses': courses
        }
        return render(request, 'course.html', context)

    def post(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        credits_ = request.POST.get('credits')

        courses = Course.objects.all()
        context = {
            'title': "Kurslar ro'yxati",
            'courses': courses
        }

        if name and credits_:
            Course.objects.create(
                name=name,
                description=description,
                credits=credits_
            )
            context['message'] = f"{name} kursi qo'shildi"
        else:
            context['message'] = "Qo'shilmadi. Ma'lumotlar to'liq emas!"

        return render(request, 'course.html', context)


class TimetableView(View):
    def get(self, request):
        timetables = Timetable.objects.all()
        classes = Class.objects.all()
        subjects = Subject.objects.all()
        teachers = Teacher.objects.all()

        context = {
            'title': "Dars jadvallari ro'yxati",
            'timetables': timetables,
            'classes': classes,
            'subjects': subjects,
            'teachers': teachers,
        }
        return render(request, 'timetable.html', context)

    def post(self, request):
        class_id = request.POST.get('class_id')
        subject_id = request.POST.get('subject_id')
        teacher_id = request.POST.get('teacher_id')
        day_of_week = request.POST.get('day_of_week')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        timetables = Timetable.objects.all()
        classes = Class.objects.all()
        subjects = Subject.objects.all()
        teachers = Teacher.objects.all()

        context = {
            'title': "Dars jadvallari ro'yxati",
            'timetables': timetables,
            'classes': classes,
            'subjects': subjects,
            'teachers': teachers,
        }

        if class_id and subject_id and teacher_id and day_of_week and start_time and end_time:
            Timetable.objects.create(
                class_id=Class.objects.get(id=class_id),
                subject_id=Subject.objects.get(id=subject_id),
                teacher_id=Teacher.objects.get(id=teacher_id),
                day_of_week=day_of_week,
                start_time=start_time,
                end_time=end_time
            )
            context['message'] = "Dars jadvali qo'shildi"
        else:
            context['message'] = "Qo'shilmadi. Ma'lumotlar to'liq emas!"

        return render(request, 'timetable.html', context)


class PaymentView(View):
    def get(self, request):
        payments = Payment.objects.all()
        students = Student.objects.all()

        context = {
            'title': "To'lovlar",
            'payments': payments,
            'students': students
        }
        return render(request, 'payment.html', context)

    def post(self, request):
        student_id = request.POST.get('student')
        amount = request.POST.get('amount')
        payment_status = request.POST.get('payment_status')
        student = Student.objects.get(id=student_id)

        payments = Payment.objects.all()
        students = Student.objects.all()
        context = {
            'title': "To'lovlar",
            'payments': payments,
            'students': students
        }

        if amount and payment_status and student:
            Payment.objects.create(
                student=student,
                amount=amount,
                payment_status=payment_status
            )
            context['message'] = "To'lov muvaffaqiyatli qo'shildi."
        else:
            context['message'] = "To'lov qo'shilmadi. Ma'lumotlar to'liq emas!"

        return render(request, 'payment.html', context)


class ExamView(View):
    def get(self, request):
        exams = Exam.objects.all()
        subjects = Subject.objects.all()

        context = {
            'title': "Imtihonlar ro'yxati",
            'exams': exams,
            'subjects': subjects
        }
        return render(request, 'exam.html', context)

    def post(self, request):
        name = request.POST.get('name')
        exam_date = request.POST.get('exam_date')
        subject_id = request.POST.get('subject')
        subject = Subject.objects.get(id=subject_id)

        exams = Exam.objects.all()
        subjects = Subject.objects.all()
        context = {
            'title': "Imtihonlar ro'yxati",
            'exams': exams,
            'subjects': subjects
        }

        if name and exam_date and subject:
            Exam.objects.create(
                name=name,
                exam_date=exam_date,
                subject=subject
            )
            context['message'] = f"{name} imtihoni qo'shildi"
        else:
            context['message'] = "Qo'shilmadi. Ma'lumotlar to'liq emas!"

        return render(request, 'exam.html', context)


class ExamResultView(View):
    def get(self, request):
        exam_results = ExamResult.objects.all()
        exams = Exam.objects.all()
        students = Student.objects.all()

        context = {
            'title': "Imtihon natijalari ro'yxati",
            'exam_results': exam_results,
            'exams': exams,
            'students': students
        }
        return render(request, 'exam_result.html', context)

    def post(self, request):
        exam_id = request.POST.get('exam')
        student_id = request.POST.get('student')
        marks_obtained = request.POST.get('marks_obtained')
        grade = request.POST.get('grade')

        exam = Exam.objects.get(id=exam_id)
        student = Student.objects.get(id=student_id)

        exam_results = ExamResult.objects.all()
        exams = Exam.objects.all()
        students = Student.objects.all()
        context = {
            'title': "Imtihon natijalari ro'yxati",
            'exam_results': exam_results,
            'exams': exams,
            'students': students
        }

        if exam and student and marks_obtained and grade:
            ExamResult.objects.create(
                exam=exam,
                student=student,
                marks_obtained=marks_obtained,
                grade=grade
            )
            context['message'] = f"{student} uchun {exam.name} imtihonida {grade} baho qo'shildi"
        else:
            context['message'] = "Qo'shilmadi. Ma'lumotlar to'liq emas!"

        return render(request, 'exam_result.html', context)
