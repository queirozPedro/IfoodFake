from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from users.api.views import UserProfileExampleViewSet
from pedidos.api.views import PedidoViewSet
from pedidos.api.views import ItemviewSet

router = SimpleRouter()

router.register("users", UserProfileExampleViewSet, basename="users")
router.register("pedidos", PedidoViewSet, basename="pedidos")
router.register("itens", ItemviewSet, basename="itens")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token-auth/", views.obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]+router.urls
