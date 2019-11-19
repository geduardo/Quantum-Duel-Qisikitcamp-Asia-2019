import json
import tornado.websocket

class DuelGroup:
    NUMBER_OF_MEMBERS = 2

    def __init__(self):
        self.members = []
        self.end = False

class MultiHandler(tornado.websocket.WebSocketHandler):
    duel_groups = []

    def open(self, *args, **kwargs):
        if len(self.duel_groups) == 0 or self.duel_groups[-1].end or len(self.duel_groups[-1].members) >= DuelGroup.NUMBER_OF_MEMBERS:
            self.duel_groups.append(DuelGroup())

        duel_group = self.duel_groups[-1]
        duel_group.members.append(self)
        self.write_message({'duel_group': len(self.duel_groups) - 1})

        if len(duel_group.members) >= DuelGroup.NUMBER_OF_MEMBERS:
            for member in duel_group.members:
                member.write_message({'message': 'ready'})

    def on_message(self, message):
        message = json.loads(message)
        duel_group = self.duel_groups[message['duel_group']]

        if duel_group.end:
            return

        duel_group.end = True
        for member in duel_group.members:
            member.write_message({'message': 'win' if member == self else 'lose'})

    def on_close(self):
        duel_group = next(filter(lambda x: self in x.members, self.duel_groups), None)
        if duel_group:
            duel_group.members.remove(self)
            if len(duel_group.members) == 0:
                self.duel_groups.remove(duel_group)
