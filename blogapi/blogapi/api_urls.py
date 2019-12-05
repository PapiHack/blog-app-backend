from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet
from articles.views import ArticleViewSet
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Backend API of our VueJS Blog App')

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('', schema_view),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
