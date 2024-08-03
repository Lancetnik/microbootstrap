from __future__ import annotations
from unittest.mock import AsyncMock, MagicMock

import litestar
import pytest

from microbootstrap import LoggingConfig, OpentelemetryConfig, PrometheusConfig, SentryConfig
from microbootstrap.console_writer import ConsoleWriter
from microbootstrap.settings import BaseBootstrapSettings


pytestmark = [pytest.mark.anyio]


@pytest.fixture(scope="session", autouse=True)
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture()
def default_litestar_app() -> litestar.Litestar:
    return litestar.Litestar()


@pytest.fixture()
def minimum_sentry_config() -> SentryConfig:
    return SentryConfig(sentry_dsn="https://examplePublicKey@o0.ingest.sentry.io/0")


@pytest.fixture()
def minimum_logging_config() -> LoggingConfig:
    return LoggingConfig(service_debug=False)


@pytest.fixture()
def minimum_prometheus_config() -> PrometheusConfig:
    return PrometheusConfig()


@pytest.fixture()
def minimum_opentelemetry_config() -> OpentelemetryConfig:
    return OpentelemetryConfig(
        service_name="test-micro-service",
        service_version="1.0.0",
        opentelemetry_endpoint="/my-engdpoint",
        opentelemetry_namespace="namespace",
        opentelemetry_container_name="container-name",
    )


@pytest.fixture()
def base_settings() -> BaseBootstrapSettings:
    return BaseBootstrapSettings()


@pytest.fixture()
def magic_mock() -> MagicMock:
    return MagicMock()


@pytest.fixture()
def async_mock() -> AsyncMock:
    return AsyncMock()


@pytest.fixture()
def console_writer() -> ConsoleWriter:
    return ConsoleWriter(writer_enabled=False)
