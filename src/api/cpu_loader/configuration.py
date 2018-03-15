from injector import Module, singleton, provider

from cpu_loader.configs.env_stats_configure import EnvStatsdConfigure
from cpu_loader.configs.env_timeout_config_factory import EnvTimeoutConfigureFactory
from cpu_loader.configs.statsd_configure import StatsdConfigure
from cpu_loader.configs.timeout_configure import TimeoutConfigure


class Configuration(Module):
    @singleton
    @provider
    def provide_timeout_configure(self) -> TimeoutConfigure:
        return EnvTimeoutConfigureFactory().create()

    @singleton
    @provider
    def provide_statsd_configure(self) -> StatsdConfigure:
        return EnvStatsdConfigure().create()

