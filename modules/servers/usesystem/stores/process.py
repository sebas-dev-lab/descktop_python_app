import threading
from typing import List


class Process:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Process, cls).__new__(cls)
                cls._instance.init()
        return cls._instance

    def init(self):
        self.on_stop_process = {}

    def set_process(self, name: str, method: callable):
        if name not in self.on_stop_process:
            self.on_stop_process[name] = []
        self.on_stop_process[name].append(method)

    def bulk_set_process(self, name: str, methods: List[callable]):
        if name not in self.on_stop_process:
            self.on_stop_process[name] = []
        for m in methods:
            self.on_stop_process[name].append(m)

    def get_process_by_nmae(self, name):
        pss = self.__dict__.items()
        try:
            return pss[name]
        except:
            return None

    def exec_methods_by_name(self, name):
        if name in self.on_stop_process:
            methods_to_execute = self.on_stop_process[name][:]
            for method in methods_to_execute:
                print('Executing:', method)
                method()
                self.on_stop_process[name].remove(method)  
        else:
            print('No methods found for name:', name)

    def get_process(self):
        attr = {}
        for key, value in self.__dict__.items():
            if not callable(value):
                attr[key] = value
        return attr
