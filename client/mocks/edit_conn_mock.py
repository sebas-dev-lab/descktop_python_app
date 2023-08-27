class EditConnMock:
    ip = '123.123.312'
    server_name = 'Mock server name'
    conection_status = True
    username = 'usermock'
    with_key = False
    with_password = True
    with_ssh = True
    local_port = 2212
    remote_port = 3366
    password = 'adas12'
    path_key = '/asdasd/path/123.pem'
    ssh_port = 1231

    def get_data(self):
        return {
            "ip": self.ip,
            "server_name": self.server_name,
            "conection_status": self.conection_status,
            "username": self.username,
            "with_key": self.with_key,
            "with_password": self.with_password,
            "with_ssh": self.with_ssh,
            "local_port": self.local_port,
            "remote_port": self.remote_port,
            "password": self.password,
            "path_key": self.path_key,
            "ssh_port": self.ssh_port,
        }
