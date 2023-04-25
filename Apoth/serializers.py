from rest_framework import serializers
from .models import Flower
class FlowerSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=1000)
    # sname = serializers.CharField(max_length=1000)
    # property = serializers.CharField(max_length=1000)
    # location = serializers.CharField(max_length=1000)
    # photo = serializers.ImageField()
    class Meta:
        model = Flower
        fields = "__all__"


# class FLowerForm(forms.Form):
#     name = forms.CharField(max_length=1000)
#     sname = forms.CharField(max_length=1000)
#     property = forms.CharField(max_length=1000)
#     location = forms.CharField(max_length=1000)
