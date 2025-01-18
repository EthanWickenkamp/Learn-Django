from django.test import TestCase

# Create your tests here.

from .models import Item
class ItemModelTest(TestCase):
    def test_create_item(self):
        # Create an item in the database
        item = Item.objects.create(
            name="Test Item",
            description="This is a test description."
        )
        
        # Check that the item was created
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.description, "This is a test description.")
        self.assertEqual(str(item), "Test Item")  # Verifies __str__ method output

    def test_item_list_count(self):
        # Create multiple items
        Item.objects.create(name="Item 1", description="First test item.")
        Item.objects.create(name="Item 2", description="Second test item.")

        # Verify the number of items in the database
        self.assertEqual(Item.objects.count(), 2)