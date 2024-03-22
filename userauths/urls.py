from django.urls import path
from userauths import views as userauths_views

urlpatterns = [
    path(
        "register/",
        userauths_views.UserRegisterView.as_view(),
        name="user_register",
    )
]
