from django.test import SimpleTestCase
from my_app.forms import TaskForm


class TestForms(SimpleTestCase):

    # Test to check if the form is valid
    def test_task_form_valid_data(self):
        # Arrange + Act
        form = TaskForm(data={
            'title': 'task1',
            'description': '1111'
        })
        # Assert
        self.assertTrue(form.is_valid())

    # Test to check if the form is not valid
    def test_task_form_no_valid_data(self):
        # Arrange + Act
        form = TaskForm(data={})
        # Assert
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
