
from django.urls import path

from . import views


urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentsDetailView),
    path('employees/', views.employeesView.as_view()),
    path('employees/<int:pk>/', views.employeesDetail.as_view()),
]