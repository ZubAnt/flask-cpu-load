import os

from cpu_loader.configs.timeout_configure import TimeoutConfigure


class EnvTimeoutConfigureFactory(object):

    @staticmethod
    def create() -> TimeoutConfigure:

        short = int(os.environ.get('SHORT_TIMEOUT', 10))
        mid = int(os.environ.get('MID_TIMEOUT', 100))
        long = int(os.environ.get('LONG_TIMEOUT', 1000))
        default = int(os.environ.get('DEFAULT_TIMEOUT', 5000))

        return TimeoutConfigure(short=short, mid=mid, long=long, default=default)
