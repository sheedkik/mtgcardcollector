import os
import uuid
import boto3
from django.shortcuts import render, redirect
from .models import Card , Collection
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import PricingForm


def home(request):
    cards = Card.objects.all()
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def card_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    id_list = card.collections.all().values_list('id')
    collections_card_doesnt_have = Collection.objects.exclude(id__in=id_list)
    pricing_form = PricingForm()
    return render(request, 'cards/detail.html', {'card': card, 'pricing_form': pricing_form, 'collections': collections_card_doesnt_have})

def cards_index(request):
  cards = Card.objects.all()
  return render(request, 'cards/index.html', {
    'cards': cards
  })

class CardCreate(CreateView):
  model = Card
  fields = ['name', 'type', 'foil', 'price', 'foilprice']

class CardUpdate(UpdateView):
  model = Card
  fields = ['name', 'type', 'foil', 'price', 'foilprice']

class CardDelete(DeleteView):
  model = Card
  success_url = '/cards'

def add_priced(request, card_id):
  form = PricingForm(request.POST)
  if form.is_valid():
    new_pricing = form.save(commit=False)
    new_pricing.card_id = card_id
    new_pricing.save()
  return redirect('detail', card_id=card_id)

class CollectionList(ListView):
  model = Collection

class CollectionDetail(DetailView):
  model = Collection

class CollectionCreate(CreateView):
  model = Collection
  fields = '__all__'

class CollectionUpdate(UpdateView):
  model = Collection
  fields = ['name', 'year']

class CollectionDelete(DeleteView):
  model = Collection
  success_url = '/collections'

def assoc_collection(request, card_id, collection_id):
  Card.objects.get(id=card_id).collections.add(collection_id)
  return redirect('detail', card_id=card_id)

def unassoc_collection(request, card_id, collection_id):
  Card.objects.get(id=card_id).collections.remove(collection_id)
  return redirect('detail', card_id=card_id)