from django.urls import path
from suggestion.views import SuggestionsListCreateView, SuggestionsRetrieveUpdateDeleteView

urlpatterns = [
    path('suggestions/', SuggestionsListCreateView.as_view(), name='suggestion-list-create'),
    path('suggestions/<uuid:pk>/', SuggestionsRetrieveUpdateDeleteView.as_view(), name='suggestion-detail'),
]
