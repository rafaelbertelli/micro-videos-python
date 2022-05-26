from pydoc import describe
import unittest
from datetime import datetime

from category.domain.entities import Category


class TestCategoryEntity(unittest.TestCase):
    def test_constructor(self):
        name = 'name'
        description = 'description'
        is_active = True
        created_at = datetime.now()
        
        category = Category(name, description, is_active, created_at)
        
        self.assertEqual(category.name, name)
        self.assertEqual(category.description, description)
        self.assertEqual(category.is_active, is_active)
        self.assertEqual(category.created_at, created_at)