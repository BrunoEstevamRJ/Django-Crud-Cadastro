from django.contrib import admin
from django.urls import path, include
from .views import form_manual

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', form_manual, name='core_form_manual'),   
    path('arquivo/', form_manual, name='core_arquivo'),
]
