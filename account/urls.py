from django.urls import path, include


urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='register'),
    path('login/', SingInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('myprofile/', profile, name='profile'),
]