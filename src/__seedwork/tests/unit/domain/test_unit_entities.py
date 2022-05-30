import unittest
from abc import ABC
from dataclasses import is_dataclass
from uuid import UUID

from __seedwork.domain.entities import Entity


class TestEntity(unittest.TestCase):
    # python -m unittest __seedwork.tests.unit.domain.test_unit_entities.TestEntity

    def test_if_it_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Entity))

    def test_if_it_is_an_absrtact_classe(self):
        self.assertIsInstance(Entity(), ABC)

    def test_property_id(self):
        entity = Entity()
        self.assertIsNotNone(entity.id)
        self.assertTrue(UUID(entity.id))

    def test_to_json(self):
        entity = Entity()
        self.assertIsNotNone(entity.to_dict())
        self.assertIsInstance(entity.to_dict(), dict)

