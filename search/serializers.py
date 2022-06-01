from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from users.models import User

from .documents import UserDocument

class UserDocumentSerializer(DocumentSerializer):
    class Meta:
        model = User
        document = UserDocument

        fields = ['id', 'username']

        # def get_location(self, obj):
        #     try:
        #         return obj.location.to_dict()
        #     except:
        #         return {}