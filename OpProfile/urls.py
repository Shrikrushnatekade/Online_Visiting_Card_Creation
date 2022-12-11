from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path("create_card/", views.createCard, name="create_card"),
    path('creation_card2/', views.createcard2, name="creation_card2"),
    path("creation_card3", views.creationcard3, name="creation_card3"),
    path("selfcard", views.selfcard, name="selfcard"),
    path("card4/", views.card4, name="card4"),
    path("service/", views.service, name="service"),
    path("logout/", views.logout, name="logout"),
]