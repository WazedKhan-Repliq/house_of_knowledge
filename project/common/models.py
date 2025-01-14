import uuid

from django.db import models

from dirtyfields import DirtyFieldsMixin

from .choices import InstanceStatus


class BaseModelWithUUIDStatus(DirtyFieldsMixin, models.Model):
    uid = models.UUIDField(
        db_column=True, unique=True, default=uuid.uuid4, editable=False
    )
    entry_by = models.ForeignKey(
        "core.User",
        models.DO_NOTHING,
        default=None,
        null=True,
        verbose_name=("entry by"),
        related_name="%(app_label)s_%(class)s_entry_by",
    )
    updated_by = models.ForeignKey(
        "core.User",
        models.DO_NOTHING,
        default=None,
        null=True,
        verbose_name=("last updated by"),
        related_name="%(app_label)s_%(class)s_updated_by",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=50,
        choices=InstanceStatus.choices,
        db_index=True,
        default=InstanceStatus.ACTIVE,
    )
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = [
            "-created_at",
        ]
