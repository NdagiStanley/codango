from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from pyfirebase import Firebase
from resources.tasks import send_notification
import celery


def is_user_logged_in(user_id):
    firebase = Firebase('https://project-8667655276128018284.firebaseio.com/')

    # Create a Firebase reference
    ref = firebase.ref('presence')
    user = ref.get()
    return True if user.get(str(user_id), None) != None else False

def terminate_task(task_id):
    query = celery.events.state.tasks_by_type('send_notice')

    for uuid, task in query:
        if uuid == task_id:
            celery.control.revoke(uuid, terminate=True)
            return True


def schedule_notification(author, resource_link, username, request, notification_type):
    task_id = notification_type + '_task_' + str(author.id)

    if not is_user_logged_in(author.id):
        exists = NotificationQueue.objects.filter(user=author, notification_type=notification_type)
        if exists:
            exists.count += 1
            exists.save()
        else:
            queue = NotificationQueue.create(
                user=author,
                notification_type=notification_type,
                count=1,
                first_interaction=username
            )

            send_notification.apply_async(
                args=[author, resource_link, request, notification_type],
                countdown=10,
                task_id=task_id
            )

    else:
        exists = NotificationQueue.objects.filter(user=author, notification_type=notification_type)
        if exists:
            exists.delete()
            terminate_task(task_id)




