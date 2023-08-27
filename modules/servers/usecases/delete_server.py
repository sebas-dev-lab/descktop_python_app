from configurations.abstracts.store_abc import SotreAbc
from helpers.errors_messages import ErrorMessagesFactory
from core.repositories.server_repository import ServerRepository
from typing import Dict, List

class DeleteServer(SotreAbc):
        def __init__(self):
            super().__init__()
            self.build_error = ErrorMessagesFactory()
            
        @ServerRepository
        def serverRepository(self):
            pass
        
        def clean_data(self) -> None:
            self.set_store("delete", None)
        
        def set_data(self, data) -> None:
            self.set_store('delete', data) # {id: "..."}
            
        def control_entity(self) -> None:
            target = self.get_store()["delete"]
            
            # Control de entiedad
            entity = self.serverRepository.get_by_id(target["id"])
            if not entity:
                msj = self.build_error.error_message("missing_entity")
                self.set_store_errors({**msj, **{"entidad": f"Server {target['id']}"}})
                self.set_error(True)

        def delete_entity(self) -> None:
            if self.get_error():
                return None
            
            target = self.get_store()["delete"]
            self.serverRepository.delete_permanent(target)
        
        def get_delete_erros(self) -> List[Dict[str, str]]:
            return self.get_store_errors()