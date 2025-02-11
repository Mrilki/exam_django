from django.urls import path, include

from . import views

app_name = 'course'

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('course/<int:pk>/edit/', views.CourseUpdateView.as_view(), name='course_update'),
    path('course/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
    path('course/create/', views.CourseCreateView.as_view(), name='course_create'),
]