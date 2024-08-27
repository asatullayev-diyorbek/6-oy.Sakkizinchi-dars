from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Maktab"
        verbose_name_plural = "Maktablar"


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Studentlar"


class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sinf"
        verbose_name_plural = "Sinflar"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.student) + ' ' + str(self.class_id)

    class Meta:
        verbose_name = "O'quvchini sinfga joylashtirish"
        verbose_name_plural = "O'quvchilarni sinfga joylashtirish"


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade_value = models.IntegerField()
    date_given = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.student) + ' ' + str(self.subject) + ' ' + str(self.grade_value)

    class Meta:
        verbose_name = "Baho"
        verbose_name_plural = "Baholar"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)


class ParentGuardian(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)  # Ota, Ona, Vasiy va h.k.
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.relationship})"

    class Meta:
        verbose_name = "Ota-ona yoki Vasiy"
        verbose_name_plural = "Ota-onalar yoki Vasiylar"


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    credits = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"


class Timetable(models.Model):
    class_id = models.ForeignKey('Class', on_delete=models.CASCADE)
    subject_id = models.ForeignKey('Subject', on_delete=models.CASCADE)
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.class_id.name} - {self.subject_id.name} ({self.day_of_week})"

    class Meta:
        verbose_name = "Dars jadvali"
        verbose_name_plural = "Dars jadvallari"


class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Kutilmoqda'),
        ('Completed', 'Tugallangan'),
        ('Failed', 'Xato')
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.student} - {self.amount} - {self.payment_status}"

    class Meta:
        verbose_name = "To'lov"
        verbose_name_plural = "To'lovlar"


class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    exam_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.subject.name})"

    class Meta:
        verbose_name = "Imtihon"
        verbose_name_plural = "Imtihonlar"


class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.student} - {self.exam.name} - {self.grade}"

    class Meta:
        verbose_name = "Imtihon natijasi"
        verbose_name_plural = "Imtihon natijalari"