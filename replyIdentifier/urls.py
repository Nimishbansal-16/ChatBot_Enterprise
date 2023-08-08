from django.urls import path
from replyIdentifier.views import ReplyIdentifierListCreateView, ReplyIdentifierRetrieveUpdateDeleteView

urlpatterns = [
    path('replyIdentifier/', ReplyIdentifierListCreateView.as_view(), name='replyIdentifier-list-create'),
    path('replyIdentifier/<uuid:pk>/', ReplyIdentifierRetrieveUpdateDeleteView.as_view(), name='replyIdentifier-detail'),
]
