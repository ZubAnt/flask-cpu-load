from datetime import datetime, timedelta

from injector import singleton, inject

from cpu_loader.configs.timeout_configure import TimeoutConfigure


@singleton
class CpuLoaderService(object):

    @inject
    def __init__(self, configure: TimeoutConfigure):
        self._configure = configure

    def load(self) -> None:
        self._load(self._configure.default)

    def load_short(self) -> None:
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

            now = datetime.now()
            if now - start > delta:
                break
