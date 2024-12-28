from .views import NewsViewSet
from django.urls import path

news_list = NewsViewSet.as_view({'get': 'list'})
urlpatterns = [
    path('editorspicks/', news_list),
]
