
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.facebook_login_view, name='facebook_login'),
    path('profile', views.profile, name='profile'),
    path('oauth/', include('social_django.urls', namespace='social')),
]
