# DjangoArrayField

Reusable Django application providing generic array field `DjangoArrayField[T]`. `T` supports Django built-ins and Django serializable objects initializable from **kwargs.

### Installation

##### PyPi:
```shell
pip install django-arrayfield
```

#### from source:
```sh
git clone https://github.com/clarin-eric/djangoarrayfield
pip install ./djangoarrayfield
```

### Testing
In order to run tests Django test configuration has to be installed as well. To run tests:
```shell
pip install ./djangoarrayfield/tests/
export DJANGO_SETTINGS_MODULE=test_arrayfield_django_conf.settings
python ./djangoarrayfield/tests/manage.py makemigations
python ./djangoarraygield/tests/manage.py test djangoarrayfield
```

### Usage
Example model using parametrized `DjangoArrayField`:

```python
from django.db import models
from djangoarrayfield import DjangoArrayField

class ExampleModel(models.Model):
    str_arrayfield: DjangoArrayField[str] = DjangoArrayField[str](name="test_array_field_str",
                                                                        verbose_name="ArrayField[str] testing field")
    int_arrayfield: DjangoArrayField[int] = DjangoArrayField[int](name="test_array_field_int",
                                                                        verbose_name="ArrayField[int] testing field")
    obj_arrayfield: DjangoArrayField[YourObject] = DjangoArrayField[YourObject](
        name="test_array_field_obj",
        verbose_name="ArrayField[YourObject] testing field")
```

### Compatibility
Currently supported (has been tested, not listed does not imply incompatibility)

##### Python
3.10, 3.11

##### Django:
4.1.7

#### DB backends:
###### Sqlite 3:
3.41.1 

### License 
DjangoArrayField is Open Source package created for internal usage at CLARIN-ERIC distributed to the public under [GPLv3](LICENSE.txt)
