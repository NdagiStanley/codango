import os
from userprofile import frequency_updates

from celery.task import task
from account.emails import SendGrid
from resources.models import Resource, NotificationQueue
from django.template import loader
from django.db.models import Count
from codango.settings.base import CODANGO_EMAIL
from django.template import Context, loader


@task
def send_recent_posts(frequency):
    recipients = frequency_updates.updates(frequency)

    # Top 5 posts on Codango
    popular_posts = Resource.objects.annotate(
        num_comments=Count('comments')).annotate(
        num_votes=Count('votes')).order_by(
        '-num_comments', '-num_votes')[:5]

    # URL to Codango
    codango_url = os.getenv('CODANGO_HOME')

    # Compose the email
    message = SendGrid.compose(
        sender='Codango <{}>'.format(CODANGO_EMAIL),
        recipient=None,
        subject="Top Posts on Codango",
        recipients=recipients,
        text=None,
        html=loader.get_template(
            'resources/popular-post-updates.html'
        ).render(Context({
            'popular_posts': popular_posts,
            'codango_url': codango_url
        }))
    )

    # send email
    response = SendGrid.send(message)
    return response


# from celery import Celery


# app = Celery('tasks', broker='amqp://localhost//')

@task(name='send_notice')
def send_notification(author, resource_link, request, notification_type):
    # Create a new task
    queue = NotificationQueue.objects.filter(
        user=author,
        notification_type=notification_type
    )
    content = queue.first_interaction
    if notification_type == 'like':
        if queue.count > 1:
            content += ' and ' + queue.count + ' other people'
        content += ' liked your resource.'
    elif notification_type == 'dislike':
        if queue.count > 1:
            content += ' and ' + queue.count + ' other people'
        content += ' down voted your resource.'
    elif notification_type == 'comment':
        if queue.count > 1:
            content += ' and ' + queue.count + ' other people'
        content += ' commented on your resource.'

    resource_email_context = {
        "subject": 'Guess what ' + author.username + '!',
        "content": content,
        "resource_link":
        request.build_absolute_uri(response_link),
        "settings_link": request.build_absolute_uri(
            '/user/' + author.username + '/settings'
        )
    }
    message = SendGrid.compose(
        'Codango <{}>'.format(CODANGO_EMAIL),
        author.email,
        'Codango: Notification',
        None,
        loader.get_template('notifications/notification-email.txt'
                            ).render(resource_email_context),
        loader.get_template('notifications/notification-email.html'
                            ).render(resource_email_context),
    )
    SendGrid.send(message)
