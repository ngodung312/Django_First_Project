from custom_admin.models import User

from celery import shared_task


@shared_task
def modify_name(username):
    user = User.objects.get(username=username)
    user.first_name = username.upper()
    user.save()

