from configurations.db.main import Base, engine
from core.repositories.server_repository import ServerRepository
from client.layouts.main.basic_main_screen import BasicMainApp
from modules.servers.usesystem.jobs.verify_ports import VerifyPorts
from modules.servers.usesystem.events.event_manager import WorkerManager
from modules.servers.usesystem.stores.process import Process


def run():
    verify_ports = VerifyPorts()
    verify_ports.thread_port_job()
    
    threads_process = Process()
    threads_process.set_process(name="verify_ports", method=verify_ports.stop_process)
    
    home = BasicMainApp()
    home.run()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    run()
