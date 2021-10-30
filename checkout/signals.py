from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Check for instance of an order sent by OrderLineItem,
    and check if it's a news
    order or an update to pre-existing one
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Check for a deletion and update accordingly
    """
    instance.order.update_total()
