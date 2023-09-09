from django.urls import path
from.views import Home,Add_student,Delete
urlpatterns = [
    path("",Home.as_view(),name='home'),
    path("add-student",Add_student.as_view(), name="add-student"),
    path("Delete", Delete.as_view(),name="Delete")
]
