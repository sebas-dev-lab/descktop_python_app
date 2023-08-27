from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from client.mocks.edit_conn_mock import EditConnMock
from client.layouts.reverse_connection.connections import ManageConnectios
from kivy.clock import Clock


class ReversConnections(BoxLayout, Widget):
    title_content = ObjectProperty()
    server_name = ObjectProperty()
    ip = ObjectProperty()
    username = ObjectProperty()
    local_port = ObjectProperty()
    remote_port = ObjectProperty()
    ssh_port = ObjectProperty()
    password = ObjectProperty()
    key = ObjectProperty()
    with_password = ObjectProperty(False)
    with_key = ObjectProperty(False)
    id = None
    checks = []

    type = ObjectProperty()
    text_submit_button = ObjectProperty()

    def __init__(self, type, id=None, dismiss=None, **kwargs):
        super(ReversConnections, self).__init__(**kwargs)
        self.type = type
        self.text_submit_button = "Editar" if type == "edit" else "Agregar"
        self.title_content = 'EDTAR CONEXIÓN DE SERVIDOR' if type == 'edit' else 'AGREGAR NUEVA CONEXIÓN CON SERVIDOR'
        self.manage_connections = ManageConnectios()
        self.id = id
        self.dismiss = dismiss
        self.build()

    def build(self):
        self.server_name.text = ""
        self.ip.text = ""
        self.username.text = ""
        self.local_port.text = ""
        self.remote_port.text = ""
        self.password.text = ""
        self.key.text = ""
        self.with_key = False
        self.with_password = False
        self.ssh_port.text = ""
        if self.type == 'edit':
            mock_server = self.manage_connections.search_by_id(self.id)
            self.id = mock_server.id
            self.server_name.text = mock_server.server_name
            self.ip.text = mock_server.ip
            self.username.text = mock_server.username
            self.local_port.text = str(mock_server.local_port)
            self.remote_port.text = str(mock_server.remote_port)
            self.password.text = mock_server.password
            self.key.text = mock_server.path_key
            self.with_key = mock_server.with_key
            self.with_password = mock_server.with_password

            if mock_server.with_key == True:
                self.checkbox_click_key(self, True, "Key")
                
            if mock_server.with_password == True:
                self.checkbox_click_password(self, True, "Password")
                                
            self.ssh_port.text = str(mock_server.ssh_port)
        if self.dismiss is not None:
            Clock.schedule_once(self.dismiss, 0.1)
        self.dismiss = None

    def btn(self):
        # Si el metodo es "agregar" se limpian los campos
        if self.type == 'add':
            result = self.manage_connections.create({
                "server_name": self.server_name.text,
                "ip": self.ip.text,
                "username": self.username.text,
                "local_port": int(self.local_port.text),
                "remote_port": int(self.remote_port.text),
                "password": self.password.text,
                "path_key": self.key.text,
                "with_key": self.with_key,
                "with_password": self.with_password,
                "ssh_port": int(self.ssh_port.text),
            })
            self.server_name.text = ""
            self.ip.text = ""
            self.username.text = ""
            self.local_port.text = ""
            self.remote_port.text = ""
            self.password.text = ""
            self.key.text = ""
            self.with_key = False
            self.with_password = False
            self.ssh_port.text = ""
        elif self.type == 'edit':
            # Si el metodo es "editar" se completan con los campos actualizados
            data_target = {
                "server_name": self.server_name.text,
                "ip": self.ip.text,
                "username": self.username.text,
                "local_port": int(self.local_port.text),
                "remote_port": int(self.remote_port.text),
                "password": self.password.text,
                "path_key": self.key.text,
                "with_key": self.with_key,
                "with_password": self.with_password,
                "ssh_port": int(self.ssh_port.text),
            }
            self.manage_connections.update({"id": self.id}, data_target)

    def checkbox_click_password(self, instance, value, topping):
        if value == True:
            self.with_password = True
            self.checks.append(topping)
        else:
            self.checks.remove(topping)
            self.with_password = False

    def checkbox_click_key(self, instance, value, topping):
        if value == True:
            self.with_key = True
            self.checks.append(topping)
        else:
            self.checks.remove(topping)
            self.with_key = False


# Cargar el archivo KV
Builder.load_file('client/layouts/reverse_connection/reversconnections.kv')
