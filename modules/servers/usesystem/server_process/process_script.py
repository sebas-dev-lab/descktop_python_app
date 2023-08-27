import subprocess
import time
from typing import List


class ProcessScriptWithoutKey:
    def __init__(self,
                 local_port: int,
                 remote_port: int,
                 username: str,
                 ip: str,
                 port: int,
                 password: str,
                 with_terminal: bool,
                 ) -> None:
        self.local_port = local_port
        self.remote_port = remote_port
        self.username = username
        self.ip = ip
        self.port = port
        self.password = password
        self.with_terminal = with_terminal

    def construct_cmd(self) -> List:
        return [
            "sshpass", "-p", self.password,
            "ssh", "-v", "-L", f"{self.local_port}:localhost:{self.remote_port}", f"{self.username}@{self.ip}", "-p", f"{self.port}"
        ]

    def run_ssh_script(self) -> None:
        if not self.with_terminal:
            self.__run_ssh_background()
        else:
            cmd = self.construct_cmd()
            self.__run_in_new_terminal(cmd)

    def __run_ssh_background(self):
        cmd = self.construct_cmd()
        cmd.append("-fN")  # -f: background, -N: no comando
        # Redirigir entrada/salida estándar a /dev/null
        stdin_redirected = open('/dev/null', 'r')
        stdout_redirected = open('/dev/null', 'w')
        stderr_redirected = open('/dev/null', 'w')

        process_script = subprocess.Popen(
            cmd, stdin=stdin_redirected, stdout=stdout_redirected, stderr=stderr_redirected)
        print(f"Process ID: {process_script.pid}")
        time.sleep(5)  # Aseguramos que el proceso se haya lanzado

    def __run_in_new_terminal(self, cmd):
            terminal_cmd = [
                "gnome-terminal", "--", "bash", "-c",
                f"{' '.join(cmd)}; read -p 'Presiona Enter para salir'"]

            subprocess.Popen(terminal_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


