from .views import ECardsViewSet, TCardsViewSet, CommentsViewSet
from django.urls import path

eCards_list = ECardsViewSet.as_view({'get': 'list', 'patch': 'partial_update'})
tCards_list = TCardsViewSet.as_view({'get': 'list', 'patch': 'partial_update'})
comments_list = CommentsViewSet.as_view({'get': 'list', 'post': 'create'})
eCards_detail = ECardsViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update'})

urlpatterns = [
    path('ecards/', eCards_list),
    path('tcards/', tCards_list),
    path('comments/', comments_list),
    path('ecards/<int:pk>/', eCards_detail),

]
