from flask import Flask
from injector import inject, singleton

from cpu_loader.blueprints.cpu_loader_blueprint import CpuLoaderBlueprint
from cpu_loader.ioc import ioc


class Application(object):

    @inject
    def __init__(self) -> None:
        self._cpu_loader = ioc.get(CpuLoaderBlueprint, scope=singleton).blueprint

    def register(self, app: Flask) -> None:
        app.register_blueprint(self._cpu_loader, url_prefix='/cpu-load')

