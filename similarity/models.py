from django.db import models


class Item(models.Model):
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.description


class Search(models.Model):
    search_input = models.CharField(max_length=200)
    similarity_indexes = models.JSONField()

    def __str__(self):
        return f'Search result for "{self.search_input}"'
