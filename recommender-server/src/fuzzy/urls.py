from django.urls import path
from fuzzy import views


urlpatterns = [
    path('forms/', views.FormView.as_view()),
    path('teacher-forms/<int:id>/', views.TeacherFormView.as_view())
]