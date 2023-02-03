from django.urls import path
from .views import RegisterView, MyLoginView, DeleteUserView, WelcomeView

from django.contrib.auth import views as auth_views

from django.conf import settings

from django.conf.urls.static import static

app_name = 'account'

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", MyLoginView.as_view(template_name='accounts/login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("welcome/", WelcomeView.as_view(), name="welcome"),
    path("delete/<int:pk>/", DeleteUserView.as_view(), name="delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)