from tortoise.models import Model
from tortoise import fields


class Resource(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=200)
    description = fields.TextField()
    resource_type = fields.CharField(max_length=50)
    url = fields.CharField(max_length=500, null=True)
    file_path = fields.CharField(max_length=300, null=True)
    category = fields.CharField(max_length=100, null=True)
    tags = fields.JSONField(null=True)
    uploaded_by = fields.ForeignKeyField(
        'models.User', related_name='resources')
    is_active = fields.BooleanField(default=True)
    view_count = fields.IntField(default=0)
    download_count = fields.IntField(default=0)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "resources"

    def __str__(self):
        return self.title
