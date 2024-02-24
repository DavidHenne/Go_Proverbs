from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:proverb_id>/", views.detail, name="detail"),
    path("random/", views.random_proverb, name="random"),
]
