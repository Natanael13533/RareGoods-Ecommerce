from django.urls import path
from appauth import views

app_name = "appauth"

urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("login", views.handle_login, name="login"),
    path("logout", views.handle_logout, name="logout"),
    path("activate/<uidb64>/<token>", views.ActivateAccountView.as_view(), name="activate"),
    path("request-reset-email", views.RequestResetEmailView.as_view(), name="reset"),
    path("set-new-password/<uidb64>/<token>", views.SetNewPasswordView.as_view(), name="new-password")
]
