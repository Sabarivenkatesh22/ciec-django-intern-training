from django.urls import path
from app.views import StudentCreateAPIView

urlpatterns = [
    path('create_student', StudentCreateAPIView.as_view(), name='student-create'),
]
