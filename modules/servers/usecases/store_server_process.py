from modules.servers.usecases.search_server import SearchServer
from typing import List, Type
from configurations.abstracts.store_queue import StoreQueue


class StoreServerProcess:
    def __init__(self, Store: Type[StoreQueue]) -> None:
        self.store = Store()
        self.search = SearchServer()

    def enqueue_all(self, *args) -> None:
        self.search.clean_data()
        servers = self.search.get_all()
        mapped_by_field = []
        for obj in servers:
            new_obj = {}
            for key in args:
                value = getattr(obj, key)
                if value is not None:
                    new_obj[key] = value
            mapped_by_field.append(new_obj)
        self.store.massive_put(mapped_by_field)

    def get_all_queue(self) -> List:
        return self.store.get_all()
