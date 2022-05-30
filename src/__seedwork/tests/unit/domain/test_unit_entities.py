import unittest
import uuid
from abc import ABC
from dataclasses import dataclass, is_dataclass
from typing import Optional
from uuid import UUID

from __seedwork.domain.entities import Entity
from __seedwork.domain.value_objects import UniqueEntityId


@dataclass(frozen=True, kw_only=True)
class StubEntity(Entity):
    prop1:Optional[str]=None
    prop2:Optional[str]=None


class TestUnitEntity(unittest.TestCase):
    # python -m unittest __seedwork.tests.unit.domain.test_unit_entities.TestUnitEntity

    def test_if_it_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Entity))

    def test_if_it_is_an_absrtact_classe(self):
        self.assertIsInstance(Entity(), ABC)

    def test_property_id(self):
        entity = Entity()
        self.assertIsNotNone(entity.id)
        self.assertTrue(UUID(entity.id))
        self.assertIsInstance(entity.id, str)
        self.assertIsInstance(entity.unique_entity_id, UniqueEntityId)

    def test_to_json(self):
        entity = Entity()
        self.assertIsNotNone(entity.to_dict())
        self.assertIsInstance(entity.to_dict(), dict)

    def test_received_id_and_others_props(self):
        entity_id = uuid.uuid4()
        entity = StubEntity(unique_entity_id=entity_id, prop1="value1", prop2="value2")

        self.assertEqual(entity.id, str(entity_id))
        self.assertEqual(entity.prop1, "value1")
        self.assertEqual(entity.prop2, "value2")
        self.assertEqual(entity.to_dict(), {"id": entity.id, "prop1": "value1", "prop2": "value2"})

    def test_received_UniqueEntityId(self):
        entity_id_1 = UniqueEntityId()
        entity_1 = StubEntity(unique_entity_id=entity_id_1)
        self.assertEqual(entity_1.id, str(entity_id_1))

        entity_id_2 = UniqueEntityId().id
        entity_2 = StubEntity(unique_entity_id=entity_id_2)
        self.assertEqual(entity_2.id, str(entity_id_2))

        entity_id_3 = str(UniqueEntityId())
        entity_3 = StubEntity(unique_entity_id=entity_id_3)
        self.assertEqual(entity_3.id, entity_id_3)

        entity_id_4 = str(UniqueEntityId().id)
        entity_4 = StubEntity(unique_entity_id=entity_id_4)
        self.assertEqual(entity_4.id, entity_id_4)

        entity_id_5 = str(uuid.uuid4())
        entity_5 = StubEntity(unique_entity_id=entity_id_5)
        self.assertEqual(entity_5.id, entity_id_5)

        entity_id_5 = uuid.uuid4()
        entity_5 = StubEntity(unique_entity_id=entity_id_5)
        self.assertEqual(entity_5.id, str(entity_id_5))
