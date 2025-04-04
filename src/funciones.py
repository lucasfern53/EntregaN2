def inicializador_de_jugadores (players):
    ## INICIALIZO LA ESTRUCTURA PARA CADA JUGADOR
    player_stats = {}
    for player in players:
        player_stats[player] = {
            'kills': 0,
            'assists': 0,
            'deaths': 0,
            'mvps': 0,
            'points': 0
        }
    return player_stats

def procesador_de_ronda (info_ronda):
    ## EN ESTA FUNCION LO QUE HAGO ES CALCULAR LOS PUNTOS DE CADA JUGADOR EN UNA RONDA
    round_points = {}
    for player, stats in info_ronda.items():
        kills = stats.get('kills', 0) ## 0 x si no hay kills
        assists = stats.get('assists', 0) ## 0 x si no hay assist
        deaths = 1 if stats.get('deaths', False) else 0 
        points = kills * 3 + assists * 1 - deaths * 1 ## hace la cuenta segun la tabla de valores que estaba en el enunciado
        round_points[player] = points ## le asigna al jugador los puntos de esa ronda
    return round_points

def actualizar_estadisticas (players_data, info_ronda, round_points):
    for player in info_ronda:
        stats = info_ronda[player]
        kills = stats.get('kills', 0)          # Kills de esta ronda (default 0)
        assists = stats.get('assists', 0)      # Assists de esta ronda (default 0)
        deaths = 1 if stats.get('deaths', False) else 0  # Muertes como 1/0
        ##Una vez obtenida la informacion de cada stats, actualizo en el diccionario principal lo que tengo en la ronda actual
        players_data[player]['kills'] += kills
        players_data[player]['assists'] += assists
        players_data[player]['deaths'] += deaths
        players_data[player]['points'] += round_points[player]

def encontrarMVP (round_points):
    playerMax = None ##para guardar el nombre del MVP
    pointsMax = -1  ##para comparar los puntos maximos 
    for player, points in round_points.items():
        if points > pointsMax:
            playerMax = player ##actualizacion de player max
            pointsMax = points ##actualizacion de puntos del player max

    return playerMax ##retornamos el MVP de la ronda


def print_round_ranking(round_num, players_data, mvp):
    print(f"\nRanking ronda {round_num}:")
    print("Jugador   | Kills | Asistencias | Muertes | MVPs | Puntos")
    print("-"*55)
    ## extraemos los puntos de los jugadores y los ordenamos de mayor a menor
    sorted_players = sorted(players_data.items(), key=lambda x: x[1]['points'], reverse=True) 
    ## un for para el que printeamos la lista ya ordenada
    for player, stats in sorted_players:
        print(f"{player.ljust(8)} | {str(stats['kills']).center(5)} | "
              f"{str(stats['assists']).center(11)} | "
              f"{str(stats['deaths']).center(7)} | "
              f"{str(stats['mvps']).center(4)} | "
              f"{stats['points']}")
    print(f"\nMVP de la ronda: {mvp}")

def print_final_ranking(players_data):
    ##Mostramos el ranking final    
    print('\n' + "="*55) 
    print("RANKING FINAL".center(55))
    print("="*55)
    print("Jugador   | Kills | Asistencias | Muertes | MVPs | Puntos")
    print("-"*55)

    ## extraemos los puntos de los jugadores y los ordenamos de mayor a menor
    sorted_players = sorted(players_data.items(), key=lambda x: x[1]['points'],reverse=True)
    for player, stats in sorted_players:
        print(f"{player.ljust(8)} | {str(stats['kills']).center(5)} | "
              f"{str(stats['assists']).center(11)} | "
              f"{str(stats['deaths']).center(7)} | "
              f"{str(stats['mvps']).center(4)} | "
              f"{stats['points']}")
    print("="*55)




