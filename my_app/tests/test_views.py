from django.test import TestCase
from my_app.models import Task


class TestViews(TestCase):

    # Test if task is created and saved in the dashboard(view)
    def test_dashboard_create_a_task(self):
        # Arrange
        task = Task(
            title="0",
            description='b'
        )
        # Act
        response = self.client.get('/dashboard')
        task.save()
        # Assert
        self.assertTemplateUsed(response, 'dashboard.html')
        self.assertEquals(str(task), task.title)


class IndexHtmlTest(TestCase):

    # Test if index.html is proper set up
    def test_index_page_returns_correctly(self):
        # Arrange + Act
        response = self.client.get('/')
        # Assert
        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(response.status_code, 200)

    # Test if register.html is proper set up
    def test_register_page_redirect_correctly(self):

        # Arrange + Act
        response = self.client.get('/register')
        # Assert
        self.assertTemplateUsed(response, 'register.html')
        self.assertEqual(response.status_code, 200)
