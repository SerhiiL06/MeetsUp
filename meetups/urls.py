from django.urls import path
from . import views

app_name = "meetups"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailMeetView.as_view(), name="detail"),
    path("<int:pk>/register/", views.DetailMeetView.as_view(), name="register"),
    path("success/", views.SuccessView.as_view(), name="success"),
]
