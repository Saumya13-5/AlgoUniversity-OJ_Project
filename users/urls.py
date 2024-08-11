# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from users import views as user_views

urlpatterns = [
    path('', user_views.welcome_view, name='welcome'),
    path('register/', user_views.register_view, name='register'),
    path('login/', user_views.login_view, name='login'),
    path('dashboard/', user_views.dashboard_view, name='dashboard'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)