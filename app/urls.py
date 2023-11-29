from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
# from app import views
# from app.views import MarcaView, ModeloView, AnioView
from .views import CarView

# router = routers.DefaultRouter()
# router.register(r'marcas/', MarcaView, basename='marca')
# router.register(r'modelos/', ModeloView, basename='modelo')
# router.register(r'anios/', AnioView, basename='anio')

urlpatterns = [
    # path("api/", include(router.urls)),
    path("cars/", CarView.as_view(), name="car-list"),
    path('docs/', include_docs_urls(title="Car_api")),    
]

# router.register(r'marcas', views.MarcaList, basename='marca')
# router.register(r'modelos', views.ModeloList, basename='modelo')
# router.register(r'anios', views.AnioList, basename='anio')