
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TodoViewSet, reset_password, login


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'todos', TodoViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/login/', login, name='login'),
    path('api/reset-password/', reset_password, name='reset_password'),
]
