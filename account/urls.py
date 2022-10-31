from django.urls import path
from . import views
app_name="account"
urlpatterns = [
    path('register/', views.register_newUser, name="register"),
    path('login/',views.login_user, name="login"),
    path('logout/',views.logout_user, name="logout"),
    path("profileupdate/", views.profileUpdate, name="profileUpdate"),
    path("profile/", views.userprofile, name="profile"),
]
