from django.db import models
from django.urls import reverse
from datetime import date

TIMES = (
   ('M', 'Morning'),
   ('A', 'Afternoon'),
   ('E', 'Evening'),
)

class Collection(models.Model):
  name = models.CharField(max_length=50)
  year = models.IntegerField(max_length=4)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('collection_detail', kwargs={'pk': self.id})

class Card(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    foil=models.BooleanField(default=False)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    foilprice=models.DecimalField(max_digits=10, decimal_places=2)
    collections = models.ManyToManyField(Collection)
    
    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'card_id': self.id})
    
    def priced_for_today(self):
       return self.prices.filter(date=date.today()).count() >= len(TIMES)

class Price_updated(models.Model):
  date = models.DateField('Price Updated Date')
  price_check = models.CharField(
    max_length=1,
    choices=TIMES,
    default=TIMES[0][0]
  )
  card = models.ForeignKey(
    Card,
    related_name='prices',
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_price_check_display()} on {self.date}"

  class Meta:
    ordering = ['-date']