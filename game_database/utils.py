from prettytable import PrettyTable

def format_ranking(ranking_str: str):
    try:
        # table = PrettyTable()
        # table.field_names = ['NOME', 'EXPERIENCIA', 'POSIÇÃO']
        table = []
        for x in range(len(ranking_str)):
            one_player_table = {}
            player_name = ranking_str[x][4]
            player_experience = ranking_str[x][2]
            one_player_table["player_name"] = player_name
            one_player_table["player_experience"] = player_experience
            table.append(one_player_table)
            # player_position = x + 1
            # table.add_row([player_name, player_experience, player_position])
        # print(table)
        return(table)
    except Exception as e:
        return ""
    
# +---------+-------------+---------+
# |   NOME  | EXPERIENCIA | POSIÇÃO |
# +---------+-------------+---------+
# |   Luis  |      29     |    1    |
# |  Daniel |      22     |    2    |
# | Matheus |      20     |    3    |
# | Matheus |      11     |    4    |
# +---------+-------------+---------+