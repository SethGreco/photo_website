from rest_framework import viewsets
from imageupload_rest.serializers import UploadImageSerializer
from hello.models import ImageModel

class UploadImageViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = UploadImageSerializer