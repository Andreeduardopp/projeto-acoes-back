from django.db import models

class Stockbase(models.Model):
    ticker = models.CharField(max_length=10)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.ticker} - {self.date}: ${self.price}"
    
class StockPrice(models.Model):
    ticker = models.CharField(max_length=10)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.ticker} - {self.date}: ${self.price}"