import unittest
from dataclasses import FrozenInstanceError, is_dataclass

from __seedwork.domain.exceptions import ValidationException
from __seedwork.domain.validators import ValidatorRules


class TestUnitValidatorRules(unittest.TestCase):

    def test_if_it_is_a_dataclass(self):
        self.assertTrue(is_dataclass(ValidatorRules))

    def test_properties_forzen(self):
        with self.assertRaises(FrozenInstanceError) as assert_error:
            validator = ValidatorRules.values("Rafael", "name")
            validator.prop = "fake prop"

        self.assertEqual(
            assert_error.exception.args[0], "cannot assign to field 'prop'")

        with self.assertRaises(FrozenInstanceError) as assert_error:
            validator = ValidatorRules.values("Rafael", "name")
            validator.value = "fake value"

        self.assertEqual(
            assert_error.exception.args[0], "cannot assign to field 'value'")

    def test_values_must_receive_value_and_prop(self):
        validator = ValidatorRules.values("Rafael", "name")

        self.assertEqual(validator.value, "Rafael")
        self.assertEqual(validator.prop, "name")

    def test_required_rule(self):

        invalid_data = [
            {'value': None, 'prop': 'name'},
            {'value': '', 'prop': 'name'},
        ]

        for data in invalid_data:
            msg = f"value: {data['value']} - prop: {data['prop']}"
            with self.assertRaises(ValidationException, msg=msg) as assert_error:
                ValidatorRules.values(data['value'], data['prop']).required()

            self.assertEqual(
                assert_error.exception.args[0], f"{data['prop']} is required")

        valid_data = [
            {'value': 'Rafael', 'prop': 'name'},
            {'value': 89, 'prop': 'name'},
            {'value': True, 'prop': 'name'},
            {'value': False, 'prop': 'name'},
        ]

        for data in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(data['value'], data['prop']).required(),
                ValidatorRules)

    def test_string_rule(self):

        invalid_data = [
            {'value': 123, 'prop': 'name'},
            {'value': True, 'prop': 'name'},
            {'value': False, 'prop': 'name'},
            {'value': [], 'prop': 'name'},
            {'value': {}, 'prop': 'name'},
        ]

        for data in invalid_data:
            msg = f"value: {data['value']} - prop: {data['prop']}"
            with self.assertRaises(ValidationException, msg=msg) as assert_error:
                ValidatorRules.values(data['value'], data['prop']).string()

            self.assertEqual(
                assert_error.exception.args[0], f"{data['prop']} must be a string")

        valid_data = [
            {'value': 'Rafael', 'prop': 'name'},
            {'value': '89', 'prop': 'name'},
            {'value': 'True', 'prop': 'name'},
            {'value': None, 'prop': 'name'},
            {'value': '', 'prop': 'name'},
        ]

        for data in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(data['value'], data['prop']).string(),
                ValidatorRules)

    def test_max_length_rule(self):

        invalid_data = [
            {'value': 'q' * 6, 'prop': 'name', 'max_length': 5},
            {'value': 'q' * 7, 'prop': 'name', 'max_length': 6},
        ]

        for data in invalid_data:
            msg = f"value: {data['value']} - prop: {data['prop']}"
            with self.assertRaises(ValidationException, msg=msg) as assert_error:
                ValidatorRules.values(
                    data['value'], data['prop']
                ).max_length(data['max_length'])

            self.assertEqual(
                assert_error.exception.args[0],
                f"{data['prop']} must be less than {data['max_length']} characters")

        valid_data = [
            {'value': 'q' * 6, 'prop': 'name', 'max_length': 6},
            {'value': 'q' * 7, 'prop': 'name', 'max_length': 10},
            {'value': None, 'prop': 'name', 'max_length': 10},
        ]

        for data in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(data['value'], data['prop']).max_length(
                    data['max_length']),
                ValidatorRules)
