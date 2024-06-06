from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import scrape_coin_data

class CoinScraperView(APIView):
    def post(self, request):
        coin_acronyms = request.data.get('coin_acronyms', [])
        if not coin_acronyms:
            return Response({"error": "No coin acronyms provided"}, status=status.HTTP_400_BAD_REQUEST)

        task = scrape_coin_data.delay(coin_acronyms)
        return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)
