from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone


def is_user_logged_in(user_id):
    sessions = Session.objects.filter(expire_date__gte=timezone.now())

    for session in sessions:
        data = session.get_decoded()
        if(data.get('_auth_user_id', 0) == user_id):
            return True

    return False


def schedule_notification(author, resource_link, username, request):
    print author.username, resource_link, username

    # exists = NotificationQueue.objects.filter(user=author, notification_type='like')
    # if exists:
    #     exists.count += 1
    #     exists.save()
    # else:
    #     queue = NotificationQueue.create(
    #         user=author,
    #         notification_type='like',
    #         count=1,
    #         first_interaction=username
    #     )
    #     schedule_notification.apply_async(
    #         args=[author, resource_link, request, 'like'],
    #         countdown=10,
    #         task_id='like_task_' + str(author.id) + '_' + str(queue.id)
    #     )
