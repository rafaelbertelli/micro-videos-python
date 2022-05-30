import unittest
from dataclasses import FrozenInstanceError, is_dataclass
from datetime import datetime

from category.domain.entities import Category


class TestCategoryUnitEntity(unittest.TestCase):
    # python -m unittest category.tests.unit.domain.test_unit_entities.TestCategoryUnitEntity

    def test_if_it_is_a_dataclass(self):
        self.assertTrue(Category)

    def test_constructor_with_params_filled(self):
        name        = 'name'
        description = 'description'
        is_active   = False
        created_at  = datetime.now()

        category = Category(
            name=name, description=description, is_active=is_active, created_at=created_at)

        self.assertIsNotNone(category.id)
        self.assertEqual(category.name, name)
        self.assertEqual(category.description, description)
        self.assertEqual(category.is_active, is_active)
        self.assertEqual(category.created_at, created_at)

    def test_constructor_with_only_required_filled(self):
        category = Category(name="name")

        self.assertEqual(category.name, "name")
        self.assertIsNone(category.description)
        self.assertTrue(category.is_active)
        self.assertIsInstance(category.created_at, datetime)

    def test_created_at_must_have_different_time(self):
        category1 = Category(name="name")
        category2 = Category(name="name")

        self.assertNotEqual(category1.created_at.timestamp(), category2.created_at.timestamp())

    def test_immutable_uuid(self):
        with self.assertRaises(FrozenInstanceError) as assert_error:
            value_object = Category(name="name")
            value_object.name = "fake name"

        self.assertEqual(assert_error.exception.args[0], "cannot assign to field 'name'")
