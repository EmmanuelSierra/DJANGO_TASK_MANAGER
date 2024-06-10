from django.test import TestCase
from my_app.models import Task


class TestModels(TestCase):

    def setUp(self):
        # Arrange + Act
        self.task1 = Task.objects.create(
            title="a_a",
            description='a'
        )

    # Testing if task has been created successfully
    def test_task_has_been_created(self):
        # Assert
        self.assertEquals(self.task1.title, 'a_a')
