from prettytable import PrettyTable

def format_ranking(ranking_str: str):
    try:
        table = PrettyTable()
        table.field_names = ['NOME', 'EXPERIENCIA', 'POSIÇÃO']
        for x in range(len(ranking_str)):
            player_name = ranking_str[x][4]
            player_experience = ranking_str[x][2]
            player_position = x + 1
            table.add_row([player_name, player_experience, player_position])
        print(table)
        return(str(table))
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