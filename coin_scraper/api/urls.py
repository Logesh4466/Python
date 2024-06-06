from django.urls import path
from .views import CoinScraperView

urlpatterns = [
    path('scrape/', CoinScraperView.as_view(), name='coin-scraper'),
]
