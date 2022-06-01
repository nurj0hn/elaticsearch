from users.serializers import UserSerializer
from .documents import UserDocument
import abc
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from django.http import HttpResponse
from elasticsearch_dsl import Q
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    SearchFilterBackend,
    CompoundSearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import UserDocument
from .serializers import UserDocumentSerializer

class ArticleDocumentView(DocumentViewSet):
    document = UserDocument
    serializer_class = UserDocumentSerializer
    filter_backends = [
        FilteringFilterBackend,
        CompoundSearchFilterBackend,
    ]
    search_fields = ('username', )

    mutli_match_search_fields = ('username',)

    filter_fields = {
        'username': 'username',
    }

















class PaginatedElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        # """This method should be overridden
        # and return a Q() expression."""
        pass

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()

            print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)


# views


class SearchUsers(PaginatedElasticSearchAPIView):
    serializer_class = UserSerializer
    document_class = UserDocument

    def generate_q_expression(self, query):
        return Q('bool',
                 should=[
                     Q('match', username=query),
                    #  Q('match', first_name=query),
                    #  Q('match', last_name=query),
                 ], minimum_should_match=1)


# class SearchUser2(APIView, LimitOffsetPagination):
#     productinventory_serializer = UserSerializer
#     search_document = UserDocument

#     def get(self, request, query=None):
#         try:
#             q = Q(
#                 "multi_match",
#                 query=query,
#                 fields=["product.name", "product.web_id", "brand.name"],
#                 fuzziness="auto",
#             ) & Q(
#                 should=[
#                     Q("match", is_default=True),
#                 ],
#                 minimum_should_match=1,
#             )

#             search = self.search_document.search().query(q)
#             response = search.execute()

#             results = self.paginate_queryset(response, request, view=self)
#             serializer = self.productinventory_serializer(results, many=True)
#             return self.get_paginated_response(serializer.data)

#         except Exception as e:
#             return HttpResponse(e, status=500)