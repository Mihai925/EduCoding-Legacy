__author__ = 'varun'

from selectable.base import ModelLookup
from selectable.registry import registry
from django.contrib.auth.models import User


class UserLookup(ModelLookup):
    model = User
    search_fields = ('email__icontains',)

    def get_item_value(self, item):
        return item.email

    def get_item_label(self, item):
        # Display for choice listings
        return u"%s (%s)" % (item.email, item.username)


registry.register(UserLookup)