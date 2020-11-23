from __future__ import annotations

from pathlib import Path

from composed_configuration import (
    ComposedConfiguration,
    ConfigMixin,
    DevelopmentBaseConfiguration,
    HerokuProductionBaseConfiguration,
    ProductionBaseConfiguration,
    TestingBaseConfiguration,
)

_pkg = 'optimal_transport_morphometry'


class OptimalTransportMorphometryConfig(ConfigMixin):
    WSGI_APPLICATION = f'{_pkg}.wsgi.application'
    ROOT_URLCONF = f'{_pkg}.urls'

    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

    @staticmethod
    def before_binding(configuration: ComposedConfiguration) -> None:
        configuration.INSTALLED_APPS += [
            f'{_pkg}.core.apps.CoreConfig',
            's3_file_field',
        ]
        configuration.REST_FRAMEWORK.update(
            {
                'DEFAULT_PAGINATION_CLASS': f'{_pkg}.core.pagination.BoundedLimitOffsetPagination',
            }
        )


class DevelopmentConfiguration(OptimalTransportMorphometryConfig, DevelopmentBaseConfiguration):
    pass


class TestingConfiguration(OptimalTransportMorphometryConfig, TestingBaseConfiguration):
    pass


class ProductionConfiguration(OptimalTransportMorphometryConfig, ProductionBaseConfiguration):
    pass


class HerokuProductionConfiguration(
    OptimalTransportMorphometryConfig, HerokuProductionBaseConfiguration
):
    pass