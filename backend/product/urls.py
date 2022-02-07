from django.urls import path
from .views import ProductDetail

from rest_framework import routers

from .views import ProductDocumentView,ProductCreate

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'product-search', ProductDocumentView, basename='product-search')


urlpatterns = [
    path('create', ProductCreate.as_view()),
    path('<int:pk>', ProductDetail.as_view()),
  ]

urlpatterns += router.urls
