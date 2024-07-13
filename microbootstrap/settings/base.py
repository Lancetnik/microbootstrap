from __future__ import annotations
import typing

import pydantic
import pydantic_settings

from microbootstrap.base.logging import base as logging_base
from microbootstrap.base.opentelemetry import OpenTelemetryInstrumentor  # noqa: TCH001
from microbootstrap.instruments import OpentelemetryConfig, SentryConfig


class BootstrapSettings(pydantic_settings.BaseSettings, SentryConfig, OpentelemetryConfig):
    debug: bool = False
    app_environment: str | None = None
    namespace: str = "default"
    service_name: str = pydantic.Field(default="micro-service")
    service_version: str = pydantic.Field(default="1.0.0")
    container_name: str | None = pydantic.Field(default=None)

    logging_log_level: int = logging_base.BASE_LOG_LEVEL
    logging_flush_level: int = logging_base.BASE_FLUSH_LEVEL
    logging_buffer_capacity: int = logging_base.BASE_CAPACITY
    logging_extra_processors: list[typing.Any] = []

    prometheus_endpoint: str | None = None
    prometheus_basic_auth: dict[str, str | int | bytes] = {}
    prometheus_headers: dict[str, typing.Any] = {}
    prometheus_timeout: int = 30
    prometheus_proxies: dict[str, str] = {}
    prometheus_tls_config: dict[str, typing.Any] = {}

    opentelemetry_endpoint: str | None = None
    opentelemetry_instruments: list[OpenTelemetryInstrumentor] = []
    opentelemetry_add_system_metrics: bool = False

    server_host: str = "0.0.0.0"  # noqa: S104
    server_port: int = 8000
    server_reload: bool = False
    server_workers_count: int = 1

    class Config:
        allow_population_by_field_name = True
