from injector import Module, singleton, provider

from cpu_loader.configs.env_timeout_config_factory import EnvTimeoutConfigureFactory
from cpu_loader.configs.timeout_configure import TimeoutConfigure


class Configuration(Module):
    @singleton
    @provider
    def provide_timeout_configure(self) -> TimeoutConfigure:
        return EnvTimeoutConfigureFactory().create()
