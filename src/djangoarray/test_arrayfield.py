from django import setup
from typing import List
from unittest import TestCase


from .models import TestArrayModel, TestObjectType


class TestArrayField(TestCase):
    test_array_obj: List[TestObjectType] = [TestObjectType("a", 1), TestObjectType("b", 2)]
    test_array_str: List[str] = ["a", "b"]
    test_array_int: List[int] = [1, 2]
    test_model_record: TestArrayModel

    def test_int(self):
        int_val: List[int] = TestArrayModel.objects.get(name="test_array_field_int")
        self.assertEqual(self.test_array_int, int_val)

    def test_str(self):
        str_val: List[str] = TestArrayModel.objects.get(name="test_array_field_str")
        self.assertEqual(self.test_array_str, str_val)

    def test_obj(self):
        obj_val: List[TestObjectType] = TestArrayModel.objects.get(name="test_array_field_obj")
        self.assertEqual(self.test_array_obj, obj_val)

    @classmethod
    def setUpClass(cls) -> None:
        setup()
        super(TestArrayField, cls).setUpClass()
        cls.test_model_record: TestArrayModel = TestArrayModel.objects.create(test_array_field_str=cls.test_array_str,
                                                                              test_array_field_int=cls.test_array_int,
                                                                              test_array_field_object=cls.test_array_obj)
        cls.test_model_record.save()

    @classmethod
    def tearDownClass(cls) -> None:
        super(TestArrayField, cls).tearDownClass()
        del cls.test_model_record
