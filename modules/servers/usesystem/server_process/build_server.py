from typing import Type
from core.models.server_model import Server
from modules.servers.usecases.search_server import SearchServer
from modules.servers.usesystem.server_process.process_script import ProcessScriptWithoutKey
from modules.servers.usesystem.server_process.kill_process import kill_process_by_port

class BuildServer:
    def __init__(self, id: str, with_terminal=True) -> None:
        self.id = id
        self.with_terminal = with_terminal
        self.server: Type[Server] = None

    # Buscar servidor
    def search_server(self):
        search = SearchServer()
        search.clean_data()
        search.set_data("id", self.id)
        self.server = search.get_by_id()

    # Correr servidor con/sin terminal
    def run_server(self):
        if self.server:
            try:
                if not self.server.with_key:
                    process_script = ProcessScriptWithoutKey(
                        local_port=self.server.local_port,
                        remote_port=self.server.remote_port,
                        username=self.server.username,
                        ip=self.server.ip,
                        port=self.server.ssh_port,
                        password=self.server.password,
                        with_terminal=self.with_terminal,
                    )
                    process_script.run_ssh_script()
            except ValueError as e:
                print(f"## [ERROR]> Error al ejecutar scritp: ==> {e}")
                return False
            return True
        else:
            return False

    def run(self, popup):
        self.search_server()
        self.run_server()
        popup.dismiss()
        
    def kill(self):
        self.search_server()
        if self.server:
            kill_process_by_port(self.server.local_port)
        else:
            print("No se encontró el servidor para matar el proceso")