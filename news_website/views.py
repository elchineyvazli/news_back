from rest_framework.viewsets import ModelViewSet
from .models import News
from .serializers import NewsSerializer
from rest_framework.renderers import JSONRenderer


class NewsViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]
    serializer_class = NewsSerializer

    def get_queryset(self):
        # id = self.request.GET.get
        tag = self.request.GET.get('tag')
        return News.objects.filter(tag=tag)
