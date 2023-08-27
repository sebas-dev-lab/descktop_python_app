import subprocess
import sys

def kill_process_by_port(port):
    try:
        command = ["lsof", "-t", f"-i:{port}"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        process_id = int(process.stdout.read().strip())
        subprocess.run(["kill", str(process_id)])
        print(f"Proceso en el puerto {port} terminado (PID: {process_id}).")
    except Exception as e:
        print(f"No se pudo terminar el proceso en el puerto {port}. Error: {e}")

def main():
    if len(sys.argv) > 1:
        port_to_check = int(sys.argv[1])
        kill_process_by_port(port_to_check)
        print(f"Recibido proceso a terminar: {port_to_check}")
    else:
        print("No se proporcionó un PID a terminar")
        sys.exit(1) 

