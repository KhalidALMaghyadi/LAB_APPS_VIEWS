from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path ('' , views.home_view  , name='heme_view'),
    path ('about/', views.about_view , name='about_view'),
    path ('password/generate/', views.password_view , name='password_view')

]