from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.popup import Popup
from client.layouts.reverse_connection.connections import ManageConnectios
from functools import partial
from kivy.clock import Clock
from modules.servers.usesystem.events.event_manager import MyThreadManager, WorkerManager
from modules.servers.usesystem.stores.process import Process
from modules.servers.usesystem.server_process.build_server import BuildServer


class InitContent(BoxLayout):
    server_list = []

    def __init__(self, dismiss=None, **kwargs):
        super(InitContent, self).__init__(**kwargs)
        self.dismiss = dismiss
        self.build()

    def build(self):
        self.server_list = []
        self.manage_connection = ManageConnectios()

        # close last event
        self.threads_process = Process()
        self.threads_process.exec_methods_by_name("rebuild_view")

        # Create event listener to rebuild view
        self.event_manager = MyThreadManager()
        self.event_manager.create_event("rebuild_view")
        self.worker_manager = WorkerManager()

        def run_management():
            self.event_manager.wait_for_event("rebuild_view")
            self._thread_function()

        self.worker = self.worker_manager.create_worker(
            name="rebuild_view", method=run_management)
        self.worker.thread_job()

        # Manage connections
        servers = self.manage_connection.search_all()
        for s in servers:
            self.server_list.append({
                "id": s.id,
                "server_name": s.server_name,
                "conection_status": s.conection_status
            })

        self.scrollview = ScrollView(size_hint=(
            1, None), size=Window.size,)

        layout = GridLayout(cols=1, size=(500, 700), padding=(
            25, 25), spacing=20, row_default_height=30,
            size_hint_y=None
        )

        layout.bind(minimum_height=layout.setter('height'))

        layout.add_widget(Label(text='Servidores Conectados', color=(
            1, 1, 1, 1), multiline=False, size_hint=(0.3, 0)))

        servers_layout = GridLayout(cols=5, padding=(
            20, 20), spacing=20, row_default_height=30, row_force_default=True, cols_minimum={0: 150, 1: 50, 2: 50, 3: 50, 4: 50},  size_hint_y=None)

        for server in self.server_list:

            grey_label = Label(
                text=server["server_name"])

            servers_layout.add_widget(grey_label)

            servers_layout.add_widget(Label(
                text="Activo" if server["conection_status"] == True else "Inactivo", height=30, size_hint=(0.3, 0.3), font_size=12, color=(0, 1, 0, 1)
                if server["conection_status"] else (
                    128, 128, 128, 128)))

            action_button = Button(
                text="Terminar" if server["conection_status"] == True else "Activar", height=30, size_hint=(0.3, 0.3), font_size=12, color=(1, 0.9, 0.9, 1))

            action_button.bind(on_release=partial(
                self.show_popup, server["id"]) if not server["conection_status"] else partial(
                self.kill_process, server["id"]))

            servers_layout.add_widget(action_button)

            edit_button = Button(
                text='Editar', font_size=12, size_hint=(0.3, 0.3))
            delete_button = Button(text='Eliminar', font_size=12, size_hint=(
                0.3, 0.3), color=(1, 0.9, 0.9, 1))

            edit_button.bind(on_press=partial(
                self.on_press_edit, server["id"]))
            delete_button.bind(on_press=partial(
                self.on_press_delete, server["id"]))

            servers_layout.add_widget(edit_button)
            servers_layout.add_widget(delete_button)

        layout.add_widget(servers_layout)

        self.scrollview.add_widget(layout)
        self.add_widget(self.scrollview)
        if self.dismiss is not None:
            Clock.schedule_once(self.dismiss, 0.1)
        self.dismiss = None

    def kill_process(self, id, instance):
        build_kill = BuildServer(id)
        build_kill.kill()

    def show_popup(self, id, instance):
        popup = Popup(title='Opciones de Ejecución',
                      size_hint=(None, None), size=(400, 200))
        popup.content = self.create_popup_content(id, popup)
        popup.open()

    def create_popup_content(self, id, popup):
        popup_layout = BoxLayout(orientation='horizontal', spacing=10)
        terminal_button = Button(
            text='En Terminal', font_size=12, size_hint=(0.3, 0.3))
        background_button = Button(
            text='En Segundo Plano', font_size=12, size_hint=(0.3, 0.3))

        build_server_terminal = BuildServer(id, with_terminal=True)
        build_server_background = BuildServer(id, with_terminal=False)

        terminal_button.bind(on_release=lambda btn: (
            build_server_terminal.run(popup), True))
        background_button.bind(on_release=lambda btn: (
            build_server_background.run(popup), True))

        popup_layout.add_widget(terminal_button)
        popup_layout.add_widget(background_button)

        return popup_layout

    def on_press_edit(self, id, edit):
        screen_manager = App.get_running_app().root
        main_screen_instance = screen_manager.get_screen(
            screen_manager.current)
        main_screen_instance.switch_content('Connection Edit', id)

    def on_press_delete(self, id, delete):
        content = BoxLayout(orientation='vertical')

        buttons_layout = BoxLayout()
        confirm_button = Button(text='Continuar')
        cancel_button = Button(text='Salir')

        confirm_button.bind(on_release=partial(self.confirm_action, id))
        cancel_button.bind(on_release=self.dismiss_popup)

        buttons_layout.add_widget(confirm_button)
        buttons_layout.add_widget(cancel_button)

        content.add_widget(buttons_layout)
        self.popup = Popup(title='¿Desea continuar?', content=content, size_hint=(
            None, None), size=(400, 200))
        self.popup.open()

    def confirm_action(self, id, instance):
        error = self.manage_connection.delete({"id": id})
        if error["error"]:
            print(error)
        else:
            self.rebuild_server_layout()
        self.dismiss_popup()

    def dismiss_popup(self, instance=None):
        self.popup.dismiss()

    def rebuild_server_layout(self):
        self.remove_widget(self.scrollview)
        self.build()

    def _thread_function(self):
        Clock.schedule_once(lambda dt: self.rebuild_server_layout())
