from kivy.uix.screenmanager import Screen
from client.layouts.abstracts.init_screen import InitScreenAPP
from client.layouts.reverse_connection.main import ReversConnections
from client.layouts.docker.main import Docker
from client.layouts.init.main import InitContent
from client.layouts.loading.main import LoadingScreen 
from kivy.uix.screenmanager import ScreenManager, Screen
from modules.servers.usesystem.stores.process import Process
from modules.servers.usesystem.events.event_manager import MyThreadManager
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock


class MainScreen(Screen):
    
    def switch_content(self, layout_name, id=None):
        dismiss = None
        if layout_name == 'Reverse Connections':
            content_layout = ReversConnections('add')
        elif layout_name == 'Connection Edit':
            dismiss = self.popup_loading()
            content_layout = ReversConnections('edit', id, dismiss=dismiss)
        elif layout_name == 'Docker':
            content_layout = Docker()
        elif layout_name == 'Inicio':
            dismiss = self.popup_loading()
            content_layout = InitContent(dismiss=dismiss)
        else:
            dismiss = self.popup_loading()
            content_layout = InitContent(dismiss=dismiss)

        self.ids.content_layout.clear_widgets()
        self.ids.content_layout.add_widget(content_layout)
   
        dismiss = None
        
    def popup_loading(self):
        self.popup = Popup(title='Cargando...', content=Label(text="Cargando pantalla..."),
                           size_hint=(None, None), size=(400, 200),)
        self.popup.open()
        return self.popup.dismiss

class BasicMainApp(InitScreenAPP):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def build(self):
        self.title = "Ding-Conn v-1.00 - PW: Sebastian Lescano"
        self.screen_manager = ScreenManager()
        self.main_screen = MainScreen()
        self.screen_manager.add_widget(self.main_screen)
        return self.screen_manager

    def on_stop(self):       
        processes = Process()
        events = MyThreadManager()

        for t, p in processes.get_process()['on_stop_process'].items():
            for ps in p:
                ps()
                print(ps)
        
        events.clear_all_events()
        

        

        