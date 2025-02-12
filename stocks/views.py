from rest_framework.response import Response
from rest_framework.decorators import api_view
from backend.settings import API_KEY
import requests


@api_view(['GET'])
def get_stock_prices(request, ticker=None):
    """Fetch historical stock prices"""

    # Get ticker from query params if not provided in the URL
    if not ticker:
        ticker = request.GET.get("ticker", None)

    if not ticker:
        return Response({"error": "Missing ticker parameter"}, status=400)

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={API_KEY}"
    response = requests.get(url).json()

    time_series = response.get("Time Series (Daily)", {})

    if not time_series:
        return Response({"error": "Invalid ticker or no data found"}, status=400)

    data = [
        {"date": date, "price": float(info["4. close"])}
        for date, info in time_series.items()
    ]

    return Response({"ticker": ticker, "data": data})
