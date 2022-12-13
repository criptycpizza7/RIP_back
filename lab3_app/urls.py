from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, CartView, CartViewSet

urlpatterns = [
    path('register', RegisterView.as_view()),
    # path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('addToCart', CartView.as_view()),
    path('cart', CartViewSet.as_view()),
]