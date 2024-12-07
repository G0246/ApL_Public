import random

def create_game_structure(players, rows):
    
    return

def print_structure(structure):
    for row in structure:
        print(''.join(row))

def simulate_game(structure, players):
    final_positions = list(range(players))
    
    for row in structure:
        for j in range(players - 1):
            if row[j] == '--|':
                final_positions[j], final_positions[j + 1] = final_positions[j + 1], final_positions[j]
    
    return final_positions

def main():
    players = int(input("Enter the number of players: "))
    rows = int(input("Enter the number of rows: "))
    
    game_structure = create_game_structure(players, rows)
    print("\nGame Structure:")
    print_structure(game_structure)

    final_positions = simulate_game(game_structure, players)
    
    print("\nFinal Positions:")
    for i, pos in enumerate(final_positions):
        print(f"Player {i + 1} ends up in position {pos + 1}")

main()