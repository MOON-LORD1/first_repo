from django.urls import path
from .views import main_view, solve_view, login_view, login_succes_view, logout_view, skip_task, account_log
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", main_view, name="main"),
    path("solve/<int:pk>", solve_view, name="solve"),
    path("login", login_view, name="login"),
    path("login-success", login_succes_view, name="login-success"),
    path("logout", logout_view, name="logout"),
    path('skip_task/', skip_task, name='skip_task'),
    path('account/<str:username>/', account_log, name='account_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



