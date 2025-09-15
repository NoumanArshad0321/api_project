
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


    path('', include(router.urls)),
    path('blogs/', views.BlogView.as_view(), name='blog-list'),
    path('comments/', views.CommentView.as_view(), name='comment-list'),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail')
]