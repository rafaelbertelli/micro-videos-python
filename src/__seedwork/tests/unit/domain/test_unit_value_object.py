# pylint: disable=protected-access

import abc
import unittest
import uuid
from dataclasses import FrozenInstanceError, dataclass, is_dataclass
from unittest.mock import patch

# from __seedwork.domain import value_objects
from __seedwork.domain.exceptions import InvalidUuidException
from __seedwork.domain.value_objects import UniqueEntityId, ValueObject


@dataclass(frozen=True)
class StubOnePropVO(ValueObject):
    prop: str


@dataclass(frozen=True)
class StubTwoPropVO(ValueObject):
    prop1: str
    prop2: str


class TestUnitValueObject(unittest.TestCase):
    # python -m unittest __seedwork.tests.unit.domain.test_unit_value_object.TestUnitValueObject

    def test_if_it_is_a_dataclass(self):
        self.assertTrue(is_dataclass(ValueObject))

    def test_if_it_is_an_abstract_class(self):
        self.assertIsInstance(ValueObject(), abc.ABC)

    def test_init_props(self):
        vo1 = StubOnePropVO(prop="value")
        self.assertEqual(vo1.prop, "value")

        vo2 = StubTwoPropVO(prop1="value1", prop2="value2")
        self.assertEqual(vo2.prop1, "value1")
        self.assertEqual(vo2.prop2, "value2")

    def test_convert_to_str(self):
        vo1 = StubOnePropVO(prop="value")
        self.assertEqual(vo1.prop, str(vo1))

        vo2 = StubTwoPropVO(prop1="value1", prop2="value2")
        self.assertEqual('{"prop1": "value1", "prop2": "value2"}', str(vo2))

    def test_immutable_uuid(self):
        with self.assertRaises(FrozenInstanceError) as assert_error:
            value_object = StubOnePropVO(prop="value")
            value_object.prop = "fake prop"

        self.assertEqual(
            assert_error.exception.args[0], "cannot assign to field 'prop'")


class TestUnitUniqueEnityId(unittest.TestCase):
    # python -m unittest __seedwork.tests.unit.domain.test_unit_value_object.TestUnitUniqueEnityId

    def test_if_it_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_throw_exception_when_id_is_not_a_uuid(self):
        with patch.object(
            UniqueEntityId,
            '_UniqueEntityId__validate',
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate
        ) as mock_validate:
            with self.assertRaises(InvalidUuidException) as assert_error:
                UniqueEntityId("fake uuid")

            mock_validate.assert_called_once()
            self.assertEqual(
                assert_error.exception.args[0], "ID must be a valid UUID")

    def test_should_pass_with_valid_uuid_str(self):
        with patch.object(
            UniqueEntityId,
            '_UniqueEntityId__validate',
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate
        ) as mock_validate:
            uuid_value = uuid.uuid4()
            value_object = UniqueEntityId(uuid_value)

            mock_validate.assert_called_once()
            self.assertEqual(value_object.id, str(uuid_value))

    def test_if_class_generates_an_uuid_str_when_it_is_not_passed(self):
        with patch.object(
            UniqueEntityId,
            '_UniqueEntityId__validate',
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate
        ) as mock_validate:
            value_object = UniqueEntityId()

            mock_validate.assert_called_once()
            self.assertIsInstance(value_object.id, str)
            uuid.UUID(value_object.id)

    def test_immutable_uuid(self):
        with self.assertRaises(FrozenInstanceError) as assert_error:
            value_object = UniqueEntityId()
            value_object.id = "fake uuid"

        self.assertEqual(
            assert_error.exception.args[0], "cannot assign to field 'id'")

    def test_convert_to_string(self):
        unique_enity_id = UniqueEntityId()
        print(unique_enity_id)

        self.assertIsInstance(unique_enity_id.id, str)
        self.assertEqual(unique_enity_id.id, str(unique_enity_id))
