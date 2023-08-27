from modules.servers.usecases.store_server_process import StoreServerProcess
from modules.servers.usesystem.stores.store_server_ports import StorePortServers
import queue
import subprocess
import time
import threading
from modules.servers.usecases.set_connection_status import SetConnectionStatus

class VerifyPorts:
    ports_to_verify = []
    ports_queue = queue.Queue()
    verify_thread = None
    running = True

    def __init__(self) -> None:
        self.ports_store = StoreServerProcess(StorePortServers)
       

    def get_ports(self):
        self.ports_to_verify = self.ports_store.get_all_queue()

    def set_ports(self):
        self.ports_store.enqueue_all("id", "local_port", "conection_status")

    def clean_ports_to_verify(self):
        self.ports_to_verify = []

    def port_exists_in_queue(self, port_to_check):
        for port in list(self.ports_queue.queue):
            if port == port_to_check:
                return True
        return False

    def add_port_to_queue(self, port_to_add):
        if not self.port_exists_in_queue(port_to_add):
            self.ports_queue.put(port_to_add)

    def verifyByPorts(self) -> None:
        while not self.ports_queue.empty():
            p = self.ports_queue.get()
            command = f"netstat -tuln | grep {p['local_port']} >> $(pwd)/process_status.log"
            current_status = None
            try:
                subprocess.check_output(
                    command, shell=True, stderr=subprocess.STDOUT, text=True)    
                current_status = True
            except subprocess.CalledProcessError:     
                current_status = False           
            set_connection_status = SetConnectionStatus(id=p["id"], status=current_status)
            if not set_connection_status.verifyConnectionStatus():
                    set_connection_status.updateConnectionStatus()
                    set_connection_status.refreshConnectiosn()

            time.sleep(0.5)

    def enqueue_ports(self):
        for p in self.ports_to_verify:
            self.add_port_to_queue(p)
    
    def manage_ports(self):
        self.set_ports()
        self.get_ports()
        self.enqueue_ports()
        self.clean_ports_to_verify()

    def run_verify(self):
        self.manage_ports()
        while self.running:
            if not self.ports_queue.empty():
                self.verifyByPorts()
            time.sleep(1)  # Sleep for 1 second to avoid excessive CPU usage
            self.manage_ports()
            
    def thread_port_job(self):
        self.running = True
        self.verify_thread = threading.Thread(target=self.run_verify)
        self.verify_thread.start()

    def stop_process(self):
        self.running = False  
        if self.verify_thread is not None:
                    self.verify_thread.join(timeout=0.1)
