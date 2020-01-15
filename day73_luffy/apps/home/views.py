
from rest_framework.generics import ListAPIView
from .import models
from . import serializers
class BannerListAPIView(ListAPIView):
    queryset = models.Banner.objects.filter(is_delete=False,is_show=True).order_by('-order').all()
    serializer_class = serializers.BannerModelSerializer




