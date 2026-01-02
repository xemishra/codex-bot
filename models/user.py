from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    telegram_id = fields.BigIntField(unique=True)
    student_name = fields.CharField(max_length=100, null=True)
    roll_number = fields.CharField(max_length=50, null=True)
    branch = fields.CharField(max_length=100, null=True)
    session = fields.IntField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} {self.roll_number} (@{self.telegram_id})"