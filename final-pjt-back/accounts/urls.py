from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.signup),
    path('profile/', views.get_accounts),
]
