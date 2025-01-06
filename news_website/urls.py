from .views import ECardsViewSet, TCardsViewSet
from django.urls import path

eCards_list = ECardsViewSet.as_view({'get': 'list', 'patch': 'partial_update'})
tCards_list = TCardsViewSet.as_view({'get': 'list', 'patch': 'partial_update'})
eCards_detail = ECardsViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update'})

urlpatterns = [
    path('ecards/', eCards_list),
    path('tcards/', tCards_list),
    path('ecards/<int:pk>/', eCards_detail),

]
