from django.db import models
from datetime import datetime

class FinanceData(models.Model):  
    date = models.DateTimeField(default=datetime.now, blank=True, null=True) 
    amount = models.IntegerField()  
    category = models.CharField(max_length=50, blank=True, null=True)  
    description = models.TextField(blank = True)  

    def __str__(self):
        return f"{self.category} - {self.amount} - {self.date.strftime('%Y-%m-%d')}"
