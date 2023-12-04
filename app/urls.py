from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
# from app import views
# from app.views import MarcaView, ModeloView, AnioView
from .api import MarcaView, ModeloView, AnioView


router = routers.DefaultRouter()
# router.register(r'car_details', CarDetailView, basename='car_detail')
router.register(r'marcas', MarcaView, basename='marca')
router.register(r'modelos', ModeloView, basename='modelo')
router.register(r'anios', AnioView, basename='anio')
# router.register(r'json/', CarView, basename='json')
# router.register(r'docs/', include_docs_urls, basename="Car_api")

urlpatterns = router.urls

# urlpatterns = [
#     # path("api/", include(router.urls)),

#     path('carmakes/', CarMakeView, name='carmake-list'),
#     path('carmodels/', CarModelView, name='carmodel-list'),
#     path('caryears/', CarYearView, name='caryear-list'),

#     path("cars_json/", CarView, name="car-list"),
    
#     path('docs/', include_docs_urls(title="Car_api")),    
# ]

# router.register(r'marcas', views.MarcaList, basename='marca')
# router.register(r'modelos', views.ModeloList, basename='modelo')
# router.register(r'anios', views.AnioList, basename='anio')