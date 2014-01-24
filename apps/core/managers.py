from django.db import models


class QuerySetManager(models.Manager):

    def __init__(self, customized_queryset=None):
        super(QuerySetManager, self).__init__()
        self.customized_queryset = customized_queryset

    def __getattr__(self, attr, *args):
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            return getattr(self.get_query_set(), attr, *args)

    def get_query_set(self):
        if self.customized_queryset:
            return self.customized_queryset(self.model)
        return super(QuerySetManager, self).get_query_set()
