from django.test import SimpleTestCase
from django.urls import reverse, resolve
from my_app.views import register, login, user_logout, dashboard


class TestUrls(SimpleTestCase):

    # Test register url is proper set up
    def test_register_url_resolves(self):
        # Arrange + Act
        url = reverse('register')
        # Assert
        self.assertEquals(resolve(url).func, register)

    # Test login url is set up correctly
    def test_login_url_resolves(self):
        # Arrange + Act
        url = reverse('login')
        # Assert
        self.assertEquals(resolve(url).func, login)

    # Test logut url is proper set up
    def test_user_logout_url_resolves(self):
        # Arrange + Act
        url = reverse('user_logout')
        # Assert
        self.assertEquals(resolve(url).func, user_logout)

    # Test dashboard url is proper set up
    def test_dashboard_resolves(self):
        # Arrange + Act
        url = reverse('dashboard')
        # Assert
        self.assertEquals(resolve(url).func, dashboard)
