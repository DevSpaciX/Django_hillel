from django.core.management import BaseCommand
from django.utils.crypto import get_random_string
from groups.models import Group,Category,Teacher,Tag
import random

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='create some courses')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        tags_query = Tag.objects.all()
        for i in range(total):
            course = Group(
                name = get_random_string(10),
                description = get_random_string(100),
                categories = Category.objects.all().order_by('?')[0],
                mentor = Teacher.objects.all().order_by('?')[0],
            )
            course.save()
            course.tags.set(random.sample(list(tags_query), random.randint(1, tags_query.count())))