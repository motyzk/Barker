from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        from django.contrib.auth.models import User
        from barker.models import Bark
        user1 = User.objects.create_user('user1')
        user2 = User.objects.create_user('user2')
        bark1 = Bark(user=user1, content='anger')
        bark2 = Bark(user=user2, content='anger')
        bark1.save()
        bark2.save()
