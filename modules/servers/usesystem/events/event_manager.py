import threading
from modules.servers.usesystem.stores.process import Process

class MyThreadManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(MyThreadManager, cls).__new__(cls)
                cls._instance.init()
        return cls._instance

    def init(self):
        self.events = {}

    def create_event(self, event_name):
        self.events[event_name] = threading.Event()

    def set_event(self, event_name):
        event = self.events.get(event_name)
        if event:
            event.set()

    def clear_event(self, event_name):
        event = self.events.get(event_name)
        if event:
            event.clear()
            
    def clear_all_events(self):
            for event_name, event in self.events.items():
                self.clear_event(event_name)
                print(f"Cleared event: {event_name}")
                
    def wait_for_event(self, event_name):
        event = self.events.get(event_name)
        if event:
            event.wait()
            


class Worker:
    def __init__(self, name, method=None, args_method=None, loop=False):
        self.name = name
        self.method = method
        self.args_method = args_method
        self._running = False
        self._worker = None
        self.threads_process = Process()
        self.loop = loop

    def thread_job(self):
        self._running = True
        self._worker = threading.Thread(target=self.run_worker)
        self._worker.start()
        self.threads_process.set_process(name=self.name, method=self.stop_process)

    def run_worker(self):
        if self.loop:
            while self._running:
                self.exec_method()
        else:
            self.exec_method()
    
    def exec_method(self):
        if self.args_method:
            self.method(self.args_method)
        else:
            self.method()

    def stop_process(self):
        self._running = False
        if self._worker is not None:
            self._worker.join(timeout=0.1)

class WorkerManager:
    def create_worker(self, name, method=None, loop=False):
        return Worker(name, method, loop)



