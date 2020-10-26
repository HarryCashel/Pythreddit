from django.db import models
import uuid

class BaseObject(models.Model):
    """
    A class that other classes will inherit from. Stores common information relative to these classes.
    Generates a random uuid when an object is created and stores the datetime the object was created.
    """
    random_eid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False, )
    date_time_created = models.DateTimeField(auto_now_add=True, db_index=True)
    class Meta: abstract = True

    @classmethod
    def get_helper(cls, **kwargs):
        try:
            return cls.objects.get(**kwargs)
        except cls.DoesNotExist:
        return None
