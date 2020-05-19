from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('delete/<city_name>/',views.delete_city,name='delete_city'),
    path('detailed/',views.deet_view,name='detailed_view'),
    path('feedback/',views.feedback_form,name='feedback'),
    path('about/',views.aboutUs,name='about')
]
