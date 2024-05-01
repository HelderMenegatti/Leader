from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class BaseModel(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name="%(class)s_created_by"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name="%(class)s_updated_by"
    )

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        user = get_user_model().get_current_user()
        self.updated_by = user
        if not self.created_by and user:
            self.created_by = user

        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["id", "created_at", "updated_at"]
