from typing import Union, Dict
from modules.servers.usecases.create_server import BuildServer
from modules.servers.usecases.delete_server import DeleteServer
from modules.servers.usecases.search_server import SearchServer
from modules.servers.usecases.edit_server import EditServer


class ServerMain:
    def set_case(self, type: str) -> Union[BuildServer, DeleteServer]:
        if type == 'create':
            return BuildServer()
        elif type == 'delete':
            return DeleteServer()
        elif type == 'search':
            return SearchServer()
        elif type == 'edit':
            return EditServer()
        else:
            raise "Tipo de proceso incorrecto."
        