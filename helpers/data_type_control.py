class DataTypeControl:
    def is_str(self, target: str):
        return isinstance(target, str)
    
    def is_int(self, target: int):
        return isinstance(target, int)
    
    def is_float(self, target: float):
        return isinstance(target, float)
    
    def is_boolean(self, target: bool):
        return isinstance(target, bool)