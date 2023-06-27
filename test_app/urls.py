from django.urls import path
from test_app.views import add_user

app_name = 'test_app'
urlpatterns = [
    path('user/', add_user, name='test_user'),
]

