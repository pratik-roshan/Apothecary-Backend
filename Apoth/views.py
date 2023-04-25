from django.shortcuts import render
from .models import Flower
from .serializers import FlowerSerializer
from rest_framework import generics
from rest_framework.renderers import JSONOpenAPIRenderer
from django.http import HttpResponse
from rest_framework.filters import SearchFilter, OrderingFilter


# Model Object -Single Flower Data
def flower_detail(request,pk):
    flo = Flower.objects.get(id=pk)
    serializer = FlowerSerializer(flo)
    Json_data = JSONOpenAPIRenderer().render(serializer.data)
    return HttpResponse(Json_data,content_type='application/json')

class Flower_Lists(generics.ListAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'sname')

# All Query set - All flower Data
def flower_list(request):
    flo = Flower.objects.all()
    serializer = FlowerSerializer(flo,many= True)
    Json_data = JSONOpenAPIRenderer().render(serializer.data)
    return HttpResponse(Json_data)


from django.db.models import Q

def flower_details(request):
    query = request.GET.get('query')
    if query:
        results = Flower.objects.filter(Q(name__icontains=query))
    else:
        results = Flower.objects.all()
    return render(request, 'search_results.html', {'results': results})



