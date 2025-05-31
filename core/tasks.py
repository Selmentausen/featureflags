import logging

from celery import shared_task
from django.db.models import Count
from django.utils import timezone

from core.models import Evaluation

logger = logging.getLogger(__name__)


@shared_task
def aggregate_flag_evaluations():
    """
    Count how many times each flag was evaluated in the last 24 h.
    Prints to stdout for now; store in a model later
    """
    since = timezone.now() - timezone.timedelta(days=1)
    rows = (
        Evaluation.objects.filter(created_at__gte=since)
        .values("flag__key")
        .annotate(total=Count("id"))
        .order_by("-total")
    )
    for row in rows:
        logger.info("%s -> %s" % (row["flag__key"], row["total"]))
    return rows.count()
