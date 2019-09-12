from django.urls import path
from employee.views import *

urlpatterns = [
    path('', employee_list, name="Employee_list"),
    path('<int:id>/details/', employee_details, name="Employee_details"),
    path('add/', employee_add, name="Add_employee"),
    path('<int:id>/edit/', employee_edit, name="Edit_employee"),
    path('<int:id>/delete/', employee_delete, name="Delete_employee"),
]