import logging

from flask import Blueprint, request, Response, json
from injector import inject, singleton

from cpu_loader.blueprints.base_blueprint import BaseBlueprint
from cpu_loader.services.cpu_loader_service import CpuLoaderService


@singleton
class CpuLoaderBlueprint(BaseBlueprint):

    @inject
    def __init__(self, service: CpuLoaderService) -> None:
        super().__init__()
        self._service = service

    @property
    def _name(self) -> str:
        return 'cpu_loader'

    def _create_blueprint(self) -> Blueprint:
        blueprint = Blueprint(self._name, __name__)

        @blueprint.route('/', methods=['GET'])
        def _default():
            self._service.load()
            return self._return_msg('[completed cpu load] default')

        @blueprint.route('/short', methods=['GET'])
        def _short():
            self._service.load_short()
            return self._return_msg('[completed cpu load] short')

        @blueprint.route('/mid', methods=['GET'])
        def _mid():
            self._service.load_mid()
            return self._return_msg('[completed cpu load] mid')

        @blueprint.route('/long', methods=['GET'])
        def _long():
            self._service.load_long()
            return self._return_msg('[completed cpu load] long')

        @blueprint.route('/random', methods=['GET'])
        def _random():
            return Response(status=200, mimetype='application/json')

        @blueprint.route('/empty', methods=['GET'])
        def _empty():
            return Response(status=200, mimetype='application/json')

        return blueprint
