# Not working as expected 14/12/24
def print_amida(amida):
    for row in range(len(amida)):
        row_str = f"{row} "  # Add row number
        for col in range(len(amida[row])):
            if amida[row][col]:
                row_str += "|--"
            else:
                row_str += "|  "
        row_str += "|"
        print(row_str)
    print()


def simulate_paths(amida, players):
    results = {}

    for player in range(players):
        current_col = player
        for row in range(len(amida)):
            if current_col < len(amida[row]) and amida[row][current_col]:
                # Move right
                current_col += 1
            elif current_col > 0 and amida[row][current_col - 1]:
                # Move left
                current_col -= 1
        results[player] = current_col
    return results

def main():
    print("Welcome to the Ghost Leg Game (Amida)!")
    
    try:
        players = int(input("Enter the number of players (columns): "))
        rows = int(input("Enter the number of rows: "))
        min_lines = int(input("Enter the minimum number of lines to add (at least 5): "))
        if min_lines < 5:
            print("The minimum number of lines must be at least 5!")
            return
    except ValueError:
        print("Invalid input. Please enter only integers.")
        return

    amida = [[False for _ in range(players - 1)] for _ in range(rows)]

    print("\nInitial Amida Diagram:")
    print_amida(amida)
    print(f"\nYou need to add at least {min_lines} lines.")

    lines_added = 0

    while lines_added < min_lines:
        try:
            row = int(input(f"Enter the row (0 to {rows - 1}) to add a line: "))
            col = int(input(f"Enter the column (0 to {players - 2}) to add a line: "))

            if not (0 <= row < rows and 0 <= col < players - 1):
                print("Invalid row or column. Try again.")
                continue

            if amida[row][col]:
                print("A line already exists here. Try a different position.")
                continue

            amida[row][col] = True
            lines_added += 1

            print(f"\nAmida Diagram after adding line at row {row}, column {col}:")
            print_amida(amida)

        except ValueError:
            print("Invalid input. Please enter only integers.")
    
    print("\nFinal Amida Diagram:")
    print_amida(amida)

    results = simulate_paths(amida, players)
    print("Player Results:")
    for player, result in results.items():
        print(f"Player {player} ends up at column {result}.")

main()