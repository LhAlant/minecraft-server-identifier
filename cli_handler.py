from identifier import Identifier

while True:
    ip = input("Server ip : ")

    try:
        port = input("Port (leave blank for default) : ")
        if not port:
            port = 25565
        else:
            port = int(port)

    except ValueError as ve:
        print("Port needs to be a number! Defaulting to 25565")
        port = 25565

    print(f"{ip}:{port}")
    server = Identifier(ip, port)
    server.start()

    if not server.online:
        print("This server is not online")
    else:
        print("Server Description : {}".format(server.description))
        print("Server version : {}".format(server.version))
        print("Ping : {}".format(server.latency))
        print("{}/{} players".format(server.player_count, server.max))
        
        player_list = ""
        for i in server.players:
            player_list += f"{i} "
        print("Online players : {}".format(player_list))

    if input("Check another server ? (y/n)").lower() != "y":
        break

    