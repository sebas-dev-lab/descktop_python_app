from configurations.db.abstracts.base_repository import Repository
from core.models.main import Server


class ServerRepository(Repository):
    def __init__(self, function):
        super(ServerRepository, self).__init__(model=Server)
        self.function = function
        
    def __call__(self, *args, **kwargs):
        self.function(*args, **kwargs)

    def create(self, data_dict) -> None:
        print(data_dict)
        super().create(data_dict)

    def update(self, filters, data_dict) -> None:
        super().update(filters, data_dict)

    def delete_logical(self, data_dict) -> None:
        super().delete_logical(data_dict)

    def delete_permanent(self, data_dict) -> None:
        super().delete_permanent(data_dict)

    def get_by_id(self, model_id):
        return super().get_by_id(model_id)

    def get_by_server_name(self, server_name):
        return super().get_by_server_name(server_name)

    def get_all(self):
        return super().get_all()

    def get_all_paginated(self, page=1, per_page=10):
        return super().get_all_paginated(page, per_page)

    def query(self, query_string, params):
        return super().query(query_string, params)
