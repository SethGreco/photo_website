from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = "hello"
urlpatterns = {

    path('', views.index, name='hello-page'),
    path('hub/', views.first, name='hub-page'),
    path('login/', LoginView.as_view(template_name='hello/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='hello/logout.html'), name="logout"),
    path('register/', views.register, name='register'),
}

