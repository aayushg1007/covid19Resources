import os
import socket
import queue
import threading

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
import requests


KV = r'''
ScrollView:
    Label:
        id: label
        text: 'You are example_name\n'
        size_hint_y: None
        height: self.texture_size[1]
'''


class Stream(App):
    def build(self):
        self.queue = queue.Queue()
        Clock.schedule_interval(self.update_stream, 0)
        threading.Thread(
            target=self.stream_worker,
            daemon=True,
        ).start()

        root = Builder.load_string(KV)
        self.label = root.ids.label

        return root

    def update_stream(self, *args):
        try:
            data = self.queue.get(block=False)
        except queue.Empty:
            return

        self.label.text += f'You won {data} points!\n'

    def stream_worker(self):
        self.response = requests.get(
            'http://localhost:5000/example_name',
            stream=True
        )

        while True:
            for data in self.response.iter_lines(
                chunk_size=1,
                decode_unicode=True
            ):
                self.queue.put(data)


Stream().run()