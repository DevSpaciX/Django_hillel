from django.core.management import BaseCommand
from django.utils.crypto import get_random_string
from groups.models import Student, Group
import random
from random import randint


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("total", type=int, help="create some courses")

    def handle(self, *args, **kwargs):
        total = kwargs["total"]
        for i in range(total):
            course = Student(
                name=get_random_string(10),
                surname=get_random_string(10),
                age=random.randint(18, 99),
                email=get_random_string(10),
                group=Group.objects.all().order_by("?")[0],
            )
            course.save()
