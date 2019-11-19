import json
import tornado.websocket

class MultiHandler(tornado.websocket.WebSocketHandler):
    waiters = set()
    messages = []

    def open(self, *args, **kwargs):
        self.waiters.add(self)
        self.write_message({'messages': self.messages})

    def on_message(self, message):
        message = json.loads(message)
        self.messages.append(message)
        for waiter in self.waiters:
            if waiter == self:
                continue
            waiter.write_message({'message': message['message']})

    def on_close(self):
        self.waiters.remove(self)
