from django.urls import path
from .views import RegisterView, UserProfileView, LogoutView, DeleteAccountView, CustomLoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("signup/", RegisterView.as_view(), name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("delete/", DeleteAccountView.as_view(), name="delete_account"),
]
