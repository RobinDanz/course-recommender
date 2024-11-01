from django.urls import path
from fuzzy import views


urlpatterns = [
    path('forms/', views.FormView.as_view()),
]