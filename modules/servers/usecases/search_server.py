from configurations.abstracts.store_abc import SotreAbc
from helpers.errors_messages import ErrorMessagesFactory
from core.repositories.server_repository import ServerRepository
from typing import Dict, List


class SearchServer(SotreAbc):
    def __init__(self):
        super().__init__()
        self.build_error = ErrorMessagesFactory()

    @ServerRepository
    def serverRepository(self):
        pass

    def clean_data(self) -> None:
        self.set_store("get_all", None)
        self.set_store("get_one", None)
        self.set_store("search_all", None)
        self.set_store("search_one", None)

    def set_data(self, target, data) -> None:
        self.set_store('search_one', {target: data})

    def get_all(self):        
        return self.serverRepository.get_all()

    def get_by_id(self):
        target = self.get_store()
        return self.serverRepository.get_by_id(target["search_one"]["id"])

    def get_delete_erros(self) -> List[Dict[str, str]]:
        return self.get_store_errors()
