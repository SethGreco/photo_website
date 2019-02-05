#The serializer converts the Django model into a Json string
# and backwards
#pk = primary key
#essentially we need to say which model we want serialized
#and what fields of the model are going to be serialized


from rest_framework import serializers
from hello.models import ImageModel

class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ('pk', 'model_pic',)
