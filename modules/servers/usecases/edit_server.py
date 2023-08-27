from configurations.abstracts.store_abc import SotreAbc
from helpers.errors_messages import ErrorMessagesFactory
from core.repositories.server_repository import ServerRepository
from typing import Dict, List

class EditServer(SotreAbc):
    def __init__(self):
        super().__init__()
        self.build_error = ErrorMessagesFactory()

    @ServerRepository
    def serverRepository(self):
        pass

    def clean_data(self) -> None:
        self.set_store("entity_target", None)
        self.set_store("entity_data", None)

    def set_target(self, target) -> None:
        self.set_store('entity_target', target)
    
    def set_target_data(self, data) -> None:
        self.set_store('entity_data', data)

    def run_edit(self) -> None:
        target = self.get_store()
        self.serverRepository.update(target["entity_target"], target["entity_data"])

    def get_delete_erros(self) -> List[Dict[str, str]]:
        return self.get_store_errors()
