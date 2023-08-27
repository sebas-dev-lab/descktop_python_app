from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty




class Docker(BoxLayout):
    pass
# Cargar el archivo KV para el Layout1
Builder.load_file('client/layouts/docker/docker.kv')