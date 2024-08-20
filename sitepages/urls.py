from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name="home_page"),
    path('privacy-policy', home, name="privacy_policy"),
    path('terms-of-service', home, name="terms_of_service"),
    path('refund-policy', home, name="refund_policy"),
    path('about-us', home, name="about_us")
]