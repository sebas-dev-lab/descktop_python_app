from abc import ABC, abstractmethod
from typing import Dict
import uuid

class SotreAbc(ABC):
    __index = ''
    __data_store={}
    __store_list = []
    __store_errors = [] # => [{type: "...", field/entidad: "...", "msj": "..."}]
    __error = False
    
    def __init__(self):
        super().__init__()
        self.__index = uuid.uuid4()
        
    def set_error(self, data: bool):
        self.__error = data
        
    def set_store_errors(self, data: Dict[str, str]) -> None:
        self.__store_errors.append(data)
    
    def set_store(self, target, data):
        self.__data_store[target] = data
    
    def set_store_list(self, data, restart: bool):
        if restart:
            self.__store_list = data
        else:
            self.__store_list.append(data)
    
    def get_store(self):
        return self.__data_store
    
    def get_store_list(self):
        return self.__store_list
    
    def get_index(self):
        return self.__index

    def get_error(self):
        return self.__error
    
    def get_store_errors(self):
        return self.__store_errors

    def get_len_store_errors(self):
        return len(self.__store_errors)