from django.urls import path
from .views import (
    LostItemListView,
    LostItemDetailView,
    LostItemCreateView,
    LostItemUpdateView,
    LostItemDeleteView,
)

app_name = 'item'  # importante para o namespace

urlpatterns = [
    path('', LostItemListView.as_view(), name='list'),
    path('item/<int:pk>/', LostItemDetailView.as_view(), name='detail'),
    path('item/create/', LostItemCreateView.as_view(), name='create'),
    path('item/<int:pk>/update/', LostItemUpdateView.as_view(), name='update'),
    path('item/<int:pk>/delete/', LostItemDeleteView.as_view(), name='delete'),
]
