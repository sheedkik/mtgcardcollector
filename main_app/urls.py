from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.cards_index, name='index'),
    path('cards/<int:card_id>/', views.card_detail, name='detail'),
    path('card/create/', views.CardCreate.as_view(), name='card_create'),
    path('card/<int:pk>/update/', views.CardUpdate.as_view(), name='card_update'),
    path('card/<int:pk>/delete/', views.CardDelete.as_view(), name='card_delete'),
    path('cards/<int:card_id>/add_priced/', views.add_priced, name='add_priced'),
    path('cards/<int:card_id>/assoc_collection/<int:collection_id>/', views.assoc_collection, name='assoc_collection'),
    path('cards/<int:card_id>/unassoc_collection/<int:collection_id>/', views.unassoc_collection, name='unassoc_collection'),
    path('collections/', views.CollectionList.as_view(), name='collection_index'),
    path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection_detail'),
    path('collections/create/', views.CollectionCreate.as_view(), name='collection_create'),
    path('collections/<int:pk>/update/', views.CollectionUpdate.as_view(), name='collections_update'),
    path('collections/<int:pk>/delete/', views.CollectionDelete.as_view(), name='collections_delete'),
]