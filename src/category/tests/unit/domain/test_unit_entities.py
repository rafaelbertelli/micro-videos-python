import unittest
from dataclasses import is_dataclass
from datetime import datetime

from category.domain.entities import Category


class TestCategoryUnitEntity(unittest.TestCase):

    def test_if_it_is_a_dataclass(self):
        category = Category('name', 'description', True, datetime.now())

        self.assertTrue(is_dataclass(category))


    def test_constructor_with_params_filled(self):
        name = 'name'
        description = 'description'
        is_active = False
        created_at = datetime.now()

        category = Category(name, description, is_active, created_at)

        self.assertEqual(category.name, name)
        self.assertEqual(category.description, description)
        self.assertEqual(category.is_active, is_active)
        self.assertEqual(category.created_at, created_at)


    def test_constructor_with_only_required_filled(self):
        category = Category("name")

        self.assertEqual(category.name, "name")
        self.assertIsNone(category.description)
        self.assertTrue(category.is_active)
        self.assertIsInstance(category.created_at, datetime)


    def test_created_at_must_have_different_time(self):
        category1 = Category("name")
        category2 = Category("name")

        self.assertNotEqual(category1.created_at.timestamp(), category2.created_at.timestamp())
