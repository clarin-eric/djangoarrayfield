from django.db import models


from .fields import DjangoArrayField


class TestObjectType(object):
    """
        Object for testing ArrayField with custom complex type
    """
    def __init__(self, test_val_1, test_val_2):
        self.test_val_1 = test_val_1,
        self.test_val_2 = test_val_2


class TestArrayModel(models.Model):
    test_array_field_str: DjangoArrayField[str] = DjangoArrayField(name="test_array_field_str",
                                                                   verbose_name="ArrayField[str] testing field")
    test_array_field_int: DjangoArrayField[int] = DjangoArrayField(name="test_array_field_int",
                                                                   verbose_name="ArrayField[int] testing field")
    test_array_field_object: DjangoArrayField[TestObjectType] = DjangoArrayField(
        name="test_array_field_obj", verbose_name="ArrayField[TestObjectType]")
