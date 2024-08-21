from django.urls import path, re_path
from .views import register, login_view, logout_view, student_dashboard

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', student_dashboard, name='dashboard'),
    re_path(r'^.*$', login_view, name='login_redirect'),  # Catch-all for root URL
]
