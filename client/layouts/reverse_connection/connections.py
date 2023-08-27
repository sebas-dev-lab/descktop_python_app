from modules.main import ServerMain
from typing import Dict, List, Union
from core.models.server_model import Server

class ManageConnectios:
    def __init__(self) -> None:
        self.server_main = ServerMain()

    def create(self, data) -> Dict[str, Union[bool, List]]:
        build = self.server_main.set_case('create')
        build.clean_data()
        build.set_data(data)
        build.control_data()
        build.encrypt_data()
        build.create_data()
        errors = build.get_errors()
        return {
            "error": True if len(errors) > 0 else False,
            "erros_list": errors
        }

    def delete(self, target: Dict[str, str]) -> Dict[str, Union[bool, List]]:
        remove = self.server_main.set_case('delete')
        remove.clean_data()
        remove.set_data(target)
        remove.control_entity()
        remove.delete_entity()
        errors = remove.get_delete_erros()
        return {
            "error": True if len(errors) > 0 else False,
            "erros_list": errors
        }

    def search_all(self) -> List[Server]:
        search = self.server_main.set_case('search')
        search.clean_data()
        return search.get_all()
    
    def search_by_id(self, id) -> Server:
        search = self.server_main.set_case('search')
        search.clean_data()
        search.set_data("id", id)
        return search.get_by_id()
    
    def update(self, filters, data) -> Server:
        edit = self.server_main.set_case('edit')
        edit.clean_data()
        edit.set_target(filters)
        edit.set_target_data(data)
        edit.run_edit()