from core.repositories.server_repository import ServerRepository
from configurations.abstracts.store_abc import SotreAbc
from modules.servers.helpers.server_data import nullable_false_data_server,fields_to_control_server
from helpers.data_type_control import DataTypeControl
from helpers.errors_messages import ErrorMessagesFactory
from typing import List, Dict


class BuildServer(SotreAbc):
    def __init__(self):
        super().__init__()
        self.build_error = ErrorMessagesFactory()
        self.control_type = DataTypeControl()

        
        

    @ServerRepository
    def __serverRepository(self):
        pass
    
    def clean_data(self) -> None:
        self.set_store("create", None)
        self.set_store_list([], True)

    def set_data(self, data) -> None:
        self.set_store('create', data)
    
    def control_data(self) -> None:
        store = self.get_store()
        # Control de datos que no pueden ser null
        for d in nullable_false_data_server:
            if d not in store["create"]:
                msj = self.build_error.error_message("missing_data").msj(d)
                self.set_store_errors({**msj, **{"field": d}})

        # Si existen errores el store de error es true y finaliza el metodo y condiciona a los siguietes
        if self.get_len_store_errors() > 0:
            self.set_error(True)
            return None
        
        # Control data types
        for key, value in fields_to_control_server.items():
            test = False
            if value == "string" and key in store["create"]:
                test = False if self.control_type.is_str(store["create"][key]) else True
            elif value == "int" and key in store["create"]:
                test = False if self.control_type.is_int(store["create"][key]) else True
            elif value == "float" and key in store["create"]:
                test = False if self.control_type.is_float(store["create"][key]) else True
            elif value == "bool" and key in store["create"]:
                test = False if self.control_type.is_boolean(store["create"][key]) else True
            
            if test:
                msj = self.build_error.error_message("wrong_type").msj(key)
                self.set_store_errors({**msj, **{"field": key}})
                
        if self.get_len_store_errors() > 0:
            self.set_error(True)
            return None
        
        
    def encrypt_data(self) -> None:
        if self.get_error():
            return None
        pass
        
    
    def create_data(self) -> None:
        if self.get_error():
            return None
    
        target = self.get_store()
        self.__serverRepository.create(target["create"])
    
    def get_errors(self) -> List[Dict[str, str]]:
        return self.get_store_errors()
    
    