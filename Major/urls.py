
from django.contrib import admin
from django.urls import path
from Apoth import views
from Apoth.views import Flower_Lists
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Flower_Lists.as_view()),
    path('floinfo/<int:pk>', views.flower_detail),
    path('floinfo/', views.flower_list),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
