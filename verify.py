import subprocess
import schedule
import time
import queue

# Define la lista de puertos que deseas verificar
ports_to_verify = [5443, 5433, 22, 3306, 443, 80, 5080, 4801, 4080, 4512, 4545, 7878, 654, 1452, 71, 81, 91, 2255]
ports_queue = queue.Queue()


def port_exists_in_queue(port_to_check):
    for port in list(ports_queue.queue):
        if port == port_to_check:
            return True
    return False


def add_port_to_queue(port_to_add):
    if not port_exists_in_queue(port_to_add):
        ports_queue.put(port_to_add)
        print(f"Se agregó el puerto {port_to_add} a la cola.")


def verifyByPorts() -> None:
    while not ports_queue.empty():
        p = ports_queue.get()
        command = f"netstat -tuln | grep {p} >> $(pwd)/process_status.log"
        print(f"Se elimino el puerto {p} a la cola.")
        try:
            process = subprocess.check_output(
                command, shell=True, stderr=subprocess.STDOUT, text=True)
            print("Proceso exitoso, puerto ocupado.")
        except subprocess.CalledProcessError:
            print("Proceso fallido, puerto libre.")

        time.sleep(0.5)


def enqueue_ports():
    for p in ports_to_verify:
        add_port_to_queue(p)


# Programa la tarea para encolar los puertos a verificar
schedule.every(5).seconds.do(enqueue_ports)

while True:
    schedule.run_pending()
    print(list(ports_queue.queue))
    if not ports_queue.empty():
        verifyByPorts()
    time.sleep(1)  # Sleep for 1 second to avoid excessive CPU usage
