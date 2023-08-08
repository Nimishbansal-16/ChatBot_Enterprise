from django.urls import path
from intent.views import IntentListCreateView, IntentRetrieveUpdateDeleteView

urlpatterns = [
    path('intents/', IntentListCreateView.as_view(), name='intent-list-create'),
    path('intents/<uuid:pk>/', IntentRetrieveUpdateDeleteView.as_view(), name='intent-detail'),
]
