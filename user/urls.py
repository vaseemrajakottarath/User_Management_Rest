from django.urls import path

from .views import UserDetailsView, UserRegisterView



urlpatterns=[
    path('api/users',UserRegisterView.as_view(),name='register'),
    path('api/users/<int:pk>',UserDetailsView.as_view(),name='details'),
]