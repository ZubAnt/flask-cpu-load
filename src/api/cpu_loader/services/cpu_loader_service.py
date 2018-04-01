from datetime import datetime, timedelta
from time import sleep

from injector import singleton, inject

from cpu_loader.configs.timeout_configure import TimeoutConfigure
from cpu_loader.controllers.stats_controller import StatsController


@singleton
class CpuLoaderService(object):

    @inject
    def __init__(self, configure: TimeoutConfigure, stats: StatsController):
        self._stats = stats
        self._configure = configure

    def load(self) -> None:
        self._load(self._configure.default)

    def load_short(self) -> None:
        self._stats.incr()
        self._load(self._configure.short)

    def load_mid(self) -> None:
        self._load(self._configure.mid)

    def load_long(self) -> None:
        self._load(self._configure.long)

    @classmethod
    def _load(cls, timeout: int) -> None:

        start = datetime.now()
        delta = timedelta(milliseconds=timeout)

        while True:

            sleep(timeout / 100)

            now = datetime.now()
            if now - start > delta:
                break
