import PySimpleGUI as sg
from identifier import Identifier

sg.theme("DarkGrey15")

layout = [
    [sg.Text("Server ip and port :"), sg.In("", key="-IP-", size=(15, 1)), sg.In("25565", key="-PORT-", size=(5, 1)), sg.Button("Search!", key="-START-")],
    [sg.Output(key="-OUTPUT-", size=(50, 9))]
]

window = sg.Window("Server checker", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "-START-":
        ip = values["-IP-"]
        
        try:
            port = int(values["-PORT-"])
        except ValueError as ve:
            print("Port needs to be a number")
            port = 25565

        server = Identifier(ip, port)
        server.start()

        if not server.online:
            print("Server doesn't exist or isn't online")
            continue

        print(server.description)
        print("{}ms".format(int(server.latency)))
        print("{}/{} players".format(server.player_count, server.max))

        player_list = ""
        print(player_list)
        for i in server.players:
            player_list += f"{i} "

        print("\nOnline players : {}".format(player_list))

window.close()