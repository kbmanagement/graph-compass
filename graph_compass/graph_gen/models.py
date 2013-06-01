from django.contrib.auth.models import User
from django.db import models


class Graph(models.Model):
    RANDOM = 'random'
    SCALE_FREE = 'scale_free'
    GRAPH_TYPE_CHOICES = (
        (RANDOM,'random'),
        (SCALE_FREE, 'scale_free')

    )
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name='owns')
    graph_type = models.CharField(max_length=10,
                                  choices = GRAPH_TYPE_CHOICES,
                                  default = RANDOM)
    size = models.IntegerField()

    def __unicode__(self):
        return u'{0}, Type: {1}, Size: {2}'.format(self.name,
                                                   self.graph_type,
                                                   self.size)
    
