
from django.urls import include, path

from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'employees', views.employeesViewSet, basename='employees')

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentsDetailView),
    # path('employees/', views.employeesView.as_view()),
    # path('employees/<int:pk>/', views.employeesDetail.as_view()),
    path('', include(router.urls))




]