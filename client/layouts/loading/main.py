from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen

class LoadingScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build()

    def build(self):
        self.orientation = "vertical"
        self.label = Label(text="Loading...")
        self.progress_bar = ProgressBar(max=100)
        
        self.add_widget(self.label)
        self.add_widget(self.progress_bar)

        # Simulación de proceso de carga
        Clock.schedule_interval(self.update_progress, 0.1)

    def update_progress(self, dt):
        # Simulación de progreso
        self.progress_bar.value += 2
        if self.progress_bar.value >= 100:
            self.progress_bar.value = 0
            
            
            

class LoadingScreenScreen(Screen):
    def __init__(self, **kwargs):
        super(LoadingScreenScreen, self).__init__(**kwargs)
        self.loadingscreen = LoadingScreen()
        self.add_widget(self.loadingscreen)