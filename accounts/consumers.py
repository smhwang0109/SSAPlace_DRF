from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    
    def disconnect(self):
        pass

    def receive(self, text_data):
        message = text_data['message']
