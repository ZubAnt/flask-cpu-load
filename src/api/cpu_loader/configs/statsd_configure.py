class StatsdConfigure(object):

    def __init__(self, host: str, port: int, prefix: str, maxudpsize: int) -> None:
        self._host = host
        self._port = port
        self._prefix = prefix
        self._maxudpsize = maxudpsize

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> int:
        return self._port

    @property
    def prefix(self) -> str:
        return self._prefix

    @property
    def maxudpsize(self) -> int:
        return self._maxudpsize
