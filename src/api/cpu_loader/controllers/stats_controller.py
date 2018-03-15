import logging

import statsd as statsd
from injector import singleton, inject

from cpu_loader.configs.statsd_configure import StatsdConfigure


@singleton
class StatsController(object):

    @inject
    def __init__(self, conf: StatsdConfigure):
        self._conf = conf
        self._client = statsd.StatsClient(host=conf.host,
                                          port=conf.port,
                                          prefix=conf.prefix,
                                          maxudpsize=conf.maxudpsize)

    def incr(self, stat=None, count=1, rate=1) -> None:
        # logging.info(f"[StatsController.incr] send to {self._conf.host}:{self._conf.port}")
        if not stat:
            self._client.incr(stat='request', count=count, rate=rate)
        self._client.incr(stat=stat, count=count, rate=rate)
