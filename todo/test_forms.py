
from django.test import TestCase
from .forms import ItemForm

# Create your tests here.
class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.error.key())
        self.assertEqual(forms.errors['name'](0))

    def test_done_field_is_not_required(self):
            form = Itemform ({'name': 'Test Todo Item'})
            self.assertTrue(form.is_valid())

    def test_field_are_expplicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(fotm.Meta.fields, ['name', 'done'])
            