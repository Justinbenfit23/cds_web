from __future__ import absolute_import, unicode_literals
from cds_web.celery import sh

@shared_task
def add(x,y):
    return x + y