ROT = "\033[91m"
GRUEN = "\033[92m"
RESET = "\033[0m"
//kommentar
def color(symbol):
    if symbol == "X":
        return ROT + symbol + RESET
    elif symbol == "O":
        return GRUEN + symbol + RESET
    else:
        return symbol

def print_field():
    print(color(field[1]) + "|" + color(field[2]) + "|" + color(field[3]))
    print(color(field[4]) + "|" + color(field[5]) + "|" + color(field[6]))
    print(color(field[7]) + "|" + color(field[8]) + "|" + color(field[9]))

def next_move():
    global run
    while True:
        player_move = input("Bitte das gewünschte Feld eingeben (oder q zum Beenden): ")
        if player_move.lower() == "q":
            print("Spiel beendet.")
            exit()  # Beendet das gesamte Programm sauber
        
        player_move = int(player_move)
        if 1 <= player_move <= 9:
            if field[player_move] == "X" or field[player_move] == "O":
                print("Spielfeld ist bereits belegt. Bitte wiederholen...")
            else:   
                return player_move
        else:
            print("Die eingegebene Zahl muss zwischen 1 und 9 liegen. Bitte Eingabe wiederholen...")

def change_player():
    global active_player
    if active_player == "X":
        active_player = "O"
    else:
        active_player = "X"

def check_win():
    # Zeilen prüfen
    if field[1] == field[2] == field[3]: return field[1]
    if field[4] == field[5] == field[6]: return field[4]
    if field[7] == field[8] == field[9]: return field[7]

    # Spalten prüfen
    if field[1] == field[4] == field[7]: return field[1]
    if field[2] == field[5] == field[8]: return field[2]
    if field[3] == field[6] == field[9]: return field[3]

    # Diagonal prüfen
    if field[1] == field[5] == field[9]: return field[1]
    if field[3] == field[5] == field[7]: return field[3]

def check_draw():
    if field[1] != "1" and field[2] != "2" and field[3] != "3" and field[4] != "4" and field[5] != "5" and field[6] != "6" and field[7] != "7" and field[8] != "8" and field[9] != "9":
        return True

# --- DIE NEUSTART-FUNKTION ---
def start_game():
    global field, active_player, run
    
    # Spielfeld und Variablen bei jedem Neustart zurücksetzen
    field = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    active_player = "X"
    run = True

    # ===== WILLKOMMENSTEXT =====
    print(GRUEN + "===========================" + RESET)
    print(GRUEN + "     WILLKOMMEN BEI" + RESET)
    print(GRUEN + "       TIC-TAC-TOE" + RESET)
    print(GRUEN + "==========================" + RESET)
    print()

    while run:
        print_field()
        player_move = next_move()
        field[player_move] = active_player
        winner = check_win()

        if winner:
            print_field()
            print("Spieler " + color(winner) + " hat gewonnen!\n")
            run = False
        elif check_draw():
            print_field()
            print("Unentschieden! Neuer Versuch?\n")
            run = False
        else:
            change_player()

    # Nach dem Ende der Schleife startet das Spiel von vorne
    print("--- NEUES SPIEL STARTEN ---")
    start_game()

# Spiel zum ersten Mal starten
start_game()