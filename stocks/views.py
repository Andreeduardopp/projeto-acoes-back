import yfinance as yf
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.cache import cache

@api_view(["GET"])
def get_stock_prices(request):
    """Fetch stock prices with a custom time range using Yahoo Finance"""

    ticker = request.GET.get("ticker", None)
    start_date = request.GET.get("start_date", None)
    end_date = request.GET.get("end_date", None)

    if not ticker:
        return Response({"error": "Missing ticker parameter"}, status=400)

    if not start_date or not end_date:
        return Response({"error": "Missing start_date or end_date"}, status=400)
    
    cache_key = f"stock_{ticker}_{start_date}_{end_date}"
    cached_data = cache.get(cache_key)

    if cached_data:
        print("Returning cached data")
        return Response(cached_data)
    
    stock = yf.Ticker(ticker)
    hist = stock.history(start=start_date, end=end_date)

    if hist.empty:
        return Response({"error": "No data found for this ticker"}, status=404)

    data = [{"date": str(date.date()), "price": round(price, 2)} for date, price in hist["Close"].items()]
    response_data = {"ticker": ticker, "data": data}
    cache.set(cache_key, response_data, timeout=60 * 60) 

    return Response({"ticker": ticker, "data": data})
