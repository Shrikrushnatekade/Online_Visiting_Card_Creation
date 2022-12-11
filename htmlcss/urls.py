from unicodedata import name
from django.urls import path
from . import views
from .views import about, acccount_verify,login

urlpatterns = [
    path('', views.index, name='index'),
    path('Registration/', views.registration, name='Registration'),
    # path('login/', login.as_view(), name= "login"),
    path('login/', views.login, name= "login"),
    path('SendE/' ,views.SendE, name='SendE' ),
    path('account_verify/<slug:token>', acccount_verify ,name="account_verify"),
    path('about/', views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]