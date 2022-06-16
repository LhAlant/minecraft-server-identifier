from socket import gaierror
from mcstatus import JavaServer
class Identifier:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        self.online = False



    def start(self):
        server = JavaServer(self.ip, self.port)

        try:
            status = server.status()

            self.online = True

            raw = status.raw

            self.description = status.description.replace("\n", " ")
            self.latency = status.latency
            self.version = status.version.name
            self.player_count = status.players.online
            self.max = status.players.max

            self.players = []
            if status.players.online:
                for i in status.players.sample:
                    self.players.append(i.name)
            if self.players == []:
                self.players.append("None")
            
        except ConnectionRefusedError as ve:
           pass
        except:
            pass