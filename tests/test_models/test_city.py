#!/usr/bin/python3
""" Defines a class TestCity for City module. """
import unittest
from models.city import City
from models.base_model import BaseModel
import datetime


class TestCity(unittest.TestCase):
    """Defines tests for City Class"""

    @classmethod
    def setUp(cls):
        """Runs for each test case.
        """
        cls.city1 = City()
        cls.city1.name = "Nairobi"

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.city1

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.city.City'>"
        self.assertEqual(str(type(self.city1)), result)

    def test_inheritance(self):
        """Test if Amenity is a subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.city1, City)
        self.assertEqual(type(self.city1), City)
        self.assertEqual(issubclass(self.city1.__class__, BaseModel), True)

    def test_types(self):
        """Test if attributes type is correct.
        """
        self.assertIsInstance(self.city1.name, str)
        self.assertEqual(type(self.city1.name), str)
        self.assertIsInstance(self.city1.id, str)
        self.assertEqual(type(self.city1.id), str)
        self.assertIsInstance(self.city1.created_at, datetime.datetime)
        self.assertIsInstance(self.city1.updated_at, datetime.datetime)
        self.assertIsInstance(self.city1.state_id, str)

    def test_save(self):
        """Test if save method is working correctly after update.
        """
        self.city1.save()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)

    def test_functions(self):
        """Test if City moudule is documented.
        """
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
        """Test if expected attributes exist.
        """
        self.assertTrue(hasattr(self.city1, 'name'))
        self.assertTrue(hasattr(self.city1, 'id'))
        self.assertTrue(hasattr(self.city1, 'created_at'))
        self.assertTrue(hasattr(self.city1, 'updated_at'))
        self.assertTrue(hasattr(self.city1, 'state_id'))

    def test_to_dict(self):
        """Test if to_dict method is working correctly.
        """
        my_model_json = self.city1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.city1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.city1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.city1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.city1.id)

    def test_unique_id(self):
        """Test if each instance is created with a unique ID.
        """
        city2 = self.city1.__class__()
        city3 = self.city1.__class__()
        city4 = self.city1.__class__()
        self.assertNotEqual(self.city1.id, city2.id)
        self.assertNotEqual(self.city1.id, city3.id)
        self.assertNotEqual(self.city1.id, city4.id)


if __name__ == '__main__':
    unittest.main()
