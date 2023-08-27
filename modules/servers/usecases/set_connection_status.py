from modules.servers.usecases.search_server import SearchServer
from modules.servers.usecases.edit_server import EditServer
from modules.servers.usesystem.events.event_manager import MyThreadManager

class SetConnectionStatus:
    def __init__(self, id: str, status: bool) -> None:
        self.id = id
        self.status = status
        self.search = SearchServer()
        try:
            self.search.set_data("id", self.id)
            self.server = self.search.get_by_id()
        except ValueError as e:
            print(f"Error al buscar servidor por id: {self.id} | Error {e}")
        
        self.edit_server = EditServer()
        self.thread = MyThreadManager()
        
            
    def verifyConnectionStatus(self):
        conn_value = getattr(self.server, "conection_status")
        return conn_value == self.status
    
    def updateConnectionStatus(self):
        try: 
            self.edit_server.clean_data()
            self.edit_server.set_target({"id": self.id})
            self.edit_server.set_target_data({
                "conection_status": self.status
            })
            self.edit_server.run_edit()
        except ValueError as e:
            print(f"Error al actualizar el estado del servidor: {self.id} | Error {e}")
    
    def refreshConnectiosn(self):
        # Emit event to rebuild view
        self.thread.set_event("rebuild_view")

