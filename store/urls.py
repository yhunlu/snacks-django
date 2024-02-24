from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register("products", views.ProductViewSet)
router.register("collections", views.CollectionViewSet)

# URLConf
urlpatterns = router.urls
