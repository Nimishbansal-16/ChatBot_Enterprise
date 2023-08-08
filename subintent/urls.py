from django.urls import path
from .views import SubIntentListCreateView, SubIntentRetrieveUpdateDeleteView

urlpatterns = [
    path('subintents/', SubIntentListCreateView.as_view(), name='subintent-list-create'),
    path('subintents/<uuid:pk>/', SubIntentRetrieveUpdateDeleteView.as_view(), name='subintent-detail'),
]
