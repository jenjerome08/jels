from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('form/', views.form, name='form'),
    path('form/nextpage', views.nextform, name='nextform'),
    path('respondent/<str:pk_test>/', views.respondent, name="respondent"),
    path('update_respondent/<str:pk>/', views.updateRespondent, name="update_respondent"),
    path('update/<str:pk>/', views.updateVaccine, name="update_vaccine"),
    path('delete/<str:pk>/', views.deleteVaccine, name="delete_vaccine"),


]