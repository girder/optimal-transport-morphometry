from celery import shared_task

from optimal_transport_morphometry.core.models import Image


@shared_task()
def image_compute_checksum(image_id: int):
    image = Image.objects.get(pk=image_id)
    image.compute_checksum()
    image.save()