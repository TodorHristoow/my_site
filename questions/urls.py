from django.urls import path
from questions.views import frequently_asked_questions

urlpatterns = (
    path('', frequently_asked_questions, name='questions'),
)
