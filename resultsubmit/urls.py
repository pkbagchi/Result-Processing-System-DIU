from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('students/', views.student_table, name='students'),
    path('student/add', views.student_add, name='student_add'),
    path('results/add', views.add_result, name='result_add'),
    path('results/', views.result_table, name='result_table'),
    path('semester/', views.add_semester, name='semester'),
    path('student/<int:id>', views.student_details, name='student_details'),
    path('result/<int:id>', views.result_details, name='result_details'),
]
