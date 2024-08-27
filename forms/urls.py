from django.urls import path
from forms import views

urlpatterns = [
    path('', views.menu, name='index'),
    path('school/', views.SchoolView.as_view(), name='school'),
    path('teacher/', views.TeacherView.as_view(), name='teacher'),
    path('student/', views.StudentView.as_view(), name='student'),
    path('class/', views.ClassView.as_view(), name='class'),
    path('subject/', views.SubjectView.as_view(), name='subject'),
    path('enrollment/', views.EnrollmentView.as_view(), name='enrollment'),
    path('grade/', views.GradeView.as_view(), name='grade'),
    path('attendance/', views.AttendanceView.as_view(), name='attendance'),

    # Qo'shimcha vazifa
    path('parent-guardian/', views.ParentGuardianView.as_view(), name='parent_guardian'),
    path('course/', views.CourseView.as_view(), name='course'),
    path('time-table/', views.TimetableView.as_view(), name='timetable'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('exam/', views.ExamView.as_view(), name='exam'),
    path('exam-result/', views.ExamResultView.as_view(), name='exam_result'),
]