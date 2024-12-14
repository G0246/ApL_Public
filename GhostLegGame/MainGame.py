def print_amida(amida, players):
    # Header
    header = " "
    for player in range(1, players + 1):
        header += f" P{player}  "
    print(header)

    # Rows and columns
    for row in range(len(amida)):
        row_str = f"{row + 1} "
        for col in range(len(amida[row])):
            if amida[row][col]:
                row_str += "|----"
            else:
                row_str += "|    "
        row_str += "|"
        print(row_str)
    print()

# BETA (Working as 14/12/24)
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

# Main function (This is killing me)
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

    amida = []

    for row_index in range(rows):
        row = []
        for col_index in range(players - 1):
            row.append(False)

        amida.append(row)

    print("\nInitial Amida Diagram:")
    print_amida(amida, players)
    print(f"\nYou need to add at least {min_lines} lines.")

    lines_added = 0

    while lines_added < min_lines:
        try:
            row = int(input(f"Enter the row (1 to {rows}) to add a line: ")) - 1
            col = int(input(f"Enter the column (1 to {players - 1}) to add a line: ")) - 1

            if not (0 <= row < rows and 0 <= col < players - 1):
                print("Invalid row or column. Try again.")
                continue

            # Check if line exist at same row
            if any(amida[row][c] for c in range(players - 1)):
                print("A line already exists in this row. Try a different row.")
                continue

            amida[row][col] = True
            lines_added += 1

            print(f"\nAmida Diagram after adding line at row {row + 1}, column {col + 1}:")
            print_amida(amida, players)

        except ValueError:
            print("Invalid input. Please enter only integers.")

    print("\nFinal Amida Diagram:")
    print_amida(amida, players)

    results = simulate_paths(amida, players)
    print("Player Results:")
    for player, result in results.items():
        print(f"Player {player + 1} ends up at column {result + 1}.")

main()