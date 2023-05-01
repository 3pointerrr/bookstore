from django.contrib import admin
from django.urls import path, include

from .views import SignupViews


urlpatterns = [
    path('signup/', SignupViews.as_view(),name='signup')
]
