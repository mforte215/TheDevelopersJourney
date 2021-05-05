from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
import uuid
from django.utils.translation import ugettext_lazy as _
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase

class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    createdBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = RichTextField()
    teaser = models.CharField(max_length=100, blank=False, default='')
    tags = TaggableManager(through=UUIDTaggedItem)
    imageUrl = models.CharField(max_length=500, blank=True)

    def __str__(self):
        selfString = self.title + " by " + self.createdBy.username
        return selfString