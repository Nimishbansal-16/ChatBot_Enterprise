from django.urls import path
from .views import OrganisationListCreateView, OrganisationRetrieveUpdateDeleteView

urlpatterns = [
    path('organisations/', OrganisationListCreateView.as_view(), name='organisation-list-create'),
    path('organisations/<uuid:pk>/', OrganisationRetrieveUpdateDeleteView.as_view(), name='organisation-detail'),
]
