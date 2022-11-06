from django.core.mail import send_mail
from Django.celery import app
from groups.models import Group, Student


@app.task
def send_emails(data):
    emails = Student.objects.all().values_list('email', flat=True)
    message = f"""
    Look at new course {data}
"""
    for email in emails:
        send_mail(
            subject='Hello !',
            from_email='mentor_course@gmail.com',
            message=message,
            recipient_list=[email]
        )


@app.task
def send_new_groups():
    courses = Group.objects.filter(rating__isnull=True).values_list('name', flat=True)
    emails = Student.objects.all().values_list('email', flat=True)
    message = f"""
    Here is some new course , look >: {','.join(courses)}
"""
    for email in emails:
        send_mail(
            subject='Interesting ?',
            from_email='mentor_course@gmail.com',
            message=message,
            recipient_list=[email]
        )
