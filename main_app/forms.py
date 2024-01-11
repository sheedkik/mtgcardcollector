from django.forms import ModelForm
from .models import Price_updated

class PricingForm(ModelForm):
  class Meta:
    model = Price_updated
    fields = ['date', 'price_check']

