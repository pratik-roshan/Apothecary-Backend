
from django.contrib import admin
from django.urls import path
from Apoth import views
from Apoth.views import Flower_Lists

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Flower_Lists.as_view()),
    path('floinfo/<int:pk>', views.flower_detail),
    path('floinfo/', views.flower_list),
]
