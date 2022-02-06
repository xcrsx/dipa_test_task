from django.test import TestCase

from .forms import MessageForm
from .models import MessageModel

DATA_FOR_TESTS = {
    "valid": {"email": "test@example.com", "message": "The text of the message"},
    "invalid": {"email": "test@example", "message": ""},
}

VALID_DATA = DATA_FOR_TESTS["valid"]
INVALID_DATA = DATA_FOR_TESTS["invalid"]


class MessageModelTest(TestCase):
    def create_new_message(
        self, email="test@example.com", message="The text of the message"
    ):
        return MessageModel.objects.create(email=email, message=message)

    def test_message_creation(self):
        new_message = self.create_new_message()
        self.assertTrue(isinstance(new_message, MessageModel))
        self.assertEqual(new_message.email, VALID_DATA["email"])
        self.assertEqual(new_message.message, VALID_DATA["message"])


class MessageFormTest(TestCase):
    def test_valid_form(self):
        form = MessageForm(VALID_DATA)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = MessageForm(INVALID_DATA)
        self.assertFalse(form.is_valid())
