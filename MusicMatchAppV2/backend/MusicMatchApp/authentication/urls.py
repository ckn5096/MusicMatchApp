from django.urls import path
from .views import RegistrationView, LoginView, HomeView, ProfileUpdateView

urlpatterns = [
   # path('register/', RegistrationView.as_view(), name='registration'),
    #path('login/', LoginView.as_view(), name='login'),
    #path('home/', HomeView.as_view(), name='home'),

    path('api/register/', RegistrationView.as_view(), name='registration'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('profile/update/' , ProfileUpdateView.as_view() , name = 'profile')
]

