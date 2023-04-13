# Changelog

## [0.1.0] - TBD

### First release
- start of CHANGELOG
- implementation of `DjangoArrayEncoder[T]` and `DjangoArrayDecoder[T]`, based on `json.JSONEncode` and `json.JSONDecode`
- implementation of `DjangoArrayField[T]` for Django, based on django.JSONField adding support for all Python built-ins and generic objects initializable from a dictionary (nested objects have to be Django serializable)
- unittests
- integration tests with `Django==4.1.7`
- pyproject.toml build config with Poetry backend