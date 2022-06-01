from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from users.models import User


PUBLISHER_INDEX = Index('user')
PUBLISHER_INDEX.settings(
    number_of_shards = 1,
    number_of_replicas =1
)

@PUBLISHER_INDEX.doc_type
class UserDocument(Document):
    id = fields.IntegerField(attr="id")
    username = fields.TextField(fields={
        "raw": {
            "type": 'keyword'
        }
    })
    class Django:
        model = User
    #     fields = ['username']