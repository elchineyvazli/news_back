from rest_framework.viewsets import ModelViewSet
from .models import ECards, TCards, Comments
from .serializers import ECardsSerializer, TCardsSerializer, CommentsSerializer
from rest_framework.renderers import JSONRenderer


class ECardsViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]
    serializer_class = ECardsSerializer

    def get_queryset(self):
        return ECards.objects.all().order_by('id')

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class TCardsViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]
    serializer_class = TCardsSerializer

    def get_queryset(self):
        return TCards.objects.all().order_by('id')

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class CommentsViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]
    serializer_class = CommentsSerializer

    def get_queryset(self):
        return Comments.objects.all().order_by('id')
