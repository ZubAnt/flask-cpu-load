class TimeoutConfigure(object):

    def __init__(self, short: int, mid: int, long: int, default: int) -> None:
        self._short = short
        self._mid = mid
        self._long = long
        self._default = default

    @property
    def short(self) -> int:
        return self._short

    @property
    def mid(self) -> int:
        return self._mid

    @property
    def long(self) -> int:
        return self._long

    @property
    def default(self) -> int:
        return self._default
