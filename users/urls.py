from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, UserListView

app_name = 'users'
urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('list/', UserListView.as_view(), name='list' ),
]
