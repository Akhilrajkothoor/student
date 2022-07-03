
from django.urls import path
from . import views
app_name="studentapp"

urlpatterns = [
    path('',views.index,name='index'),
   path('student/<int:student_id>/',views.detail,name='detail'),
    path('add_student/',views.add_student,name='add_student'),
   path('update/<int:id>/', views.update, name='update'),
     path('delete/<int:id>/', views.delete, name='delete'),
 ]
