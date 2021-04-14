from django.contrib import admin
from django.urls import path
from srt import views

urlpatterns = [
    path('', views.home,name='home'),
    path('p/', views.premium,name='premium'),
    path("db/", views.short, name="short"),
    path("i/<str:lk>/", views.search, name="search"),
    path("is/", views.insearch, name="insearch"),
    path("signup/", views.handleSignup, name="handleSignup"),
	path("login/", views.handleLogin, name="handleLogin"),
	path("logout/", views.handleLogout, name="handleLogout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("db2/", views.pshort, name="short"),
    path("j/<str:lk>/", views.psearch, name="search"),
    path("js/", views.pinsearch, name="insearch"),
    path("db3/", views.cshort, name="short"),
    path("c/<str:lk>/", views.csearch, name="search"),
    path("cs/", views.cinsearch, name="insearch"),
    path("customdashboard/", views.customdashboard, name="customdashboard"),
   
]
