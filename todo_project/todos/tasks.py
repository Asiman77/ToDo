from celery import shared_task
from .models import Todo
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings

@shared_task
def delete_completed_todos():
    Todo.objects.filter(is_finished=True).delete()

@shared_task
def send_overdue_reminders():
    overdue_todos = Todo.objects.filter(due_date=timezone.now(), is_finished=False)
    email_list = overdue_todos.values_list('author__email', flat=True).distinct()

    for email in email_list:
        send_mail(
            'Overdue Todo Reminder',
            "You haven't completed your todo.",
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )