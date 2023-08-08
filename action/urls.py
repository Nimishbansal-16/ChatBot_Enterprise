from django.urls import path
from .views import ActionListCreateView, ActionRetrieveUpdateDeleteView

urlpatterns = [
    path('actions/', ActionListCreateView.as_view(), name='action-list-create'),
    path('actions/<uuid:pk>/', ActionRetrieveUpdateDeleteView.as_view(), name='action-detail'),
]
