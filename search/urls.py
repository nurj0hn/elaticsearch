from django.urls import path, include

# from search.views import ArticleDocumentView
from rest_framework import routers
from .views import ArticleDocumentView
from .views import SearchUsers

router = routers.SimpleRouter(trailing_slash=False)

router.register('haha', ArticleDocumentView, basename='article-search')


urlpatterns = [
    path('user/<str:query>/', SearchUsers.as_view()),
    path('', include(router.urls))
]
# urlpatterns += router.urls