from typing import Dict, Union
from abc import ABC, abstractmethod

# Productos


class ErrorMessages(ABC):

    @abstractmethod
    def msj(self, error: str) ->  Dict[str, str]:
        pass


class MissingDataMessages(ErrorMessages):
    type = "missing_data"

    def msj(self, error: str) ->  Dict[str, str]:
        return {
            "msj": f"Dato requerido para el campo: {error}",
            "type": self.type
        }


class WrongDataTypeMessages(ErrorMessages):
    type = "wrong_type"

    def msj(self, error: str) ->  Dict[str, str]:
        return {
            "msj": f"Tipo de dato incorrecto en el campo: {error}",
            "type": self.type
        }
        

class MissingEntityMessages(ErrorMessages):
    type = "missing_entity"

    def msj(self, error: str) ->  Dict[str, str]:
        return {
            "msj": f"No se encuentra el elemento a eliminar: {error}",
            "type": self.type
        }
        
        
class ErrorMessagesFactory:
    def error_message(self, type: str) ->  Union[MissingDataMessages, WrongDataTypeMessages]:
        if type == "missing_data":
            return MissingDataMessages()
        elif type == "wrong_type":
            return WrongDataTypeMessages()
        elif type == "missing_entity":
            return MissingEntityMessages()
        else:
            raise ValueError("Typo inválido")