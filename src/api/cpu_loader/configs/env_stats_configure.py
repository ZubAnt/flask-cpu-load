import os

from cpu_loader.configs.statsd_configure import StatsdConfigure


class EnvStatsdConfigure(object):

    @staticmethod
    def create() -> StatsdConfigure:
        host = os.environ.get('STATSD_HOST', 'localhost')
        port = int(os.environ.get('STATSD_PORT', 8125))
        prefix = os.environ.get('STATSD_PREIX', 'API')
        maxudpsize = int(os.environ.get('STATSD_MAXUDPSIZE', 512))

        return StatsdConfigure(host=host, port=port, prefix=prefix, maxudpsize=maxudpsize)
