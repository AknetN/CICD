from django.test import TestCase
from test_app.form import UserForm

# Create your tests here.
class AddUserTestCase(TestCase):
    def test_invalid_user_form(self):
        form = UserForm()
        self.assertEqual(form.is_valid(), False)
    
    def test_valid_user_form(self):
        data = {'username': 'julia', 'email': 'test@example.com', 'password': '1234'}
        form = UserForm(data)
        self.assertEqual(form.is_valid(), True)
