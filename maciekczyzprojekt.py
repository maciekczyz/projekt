import random

def print_menu():
    print("\nWitaj w Kasynie!")
    print("1. Ruletka")
    print("2. Blackjack")
    print("3. Rosyjska ruletka")
    print("4. Poker")
    print("5. Kółko-krzyżyk")
    print("6. Wyścigi konne")
    print("7. Sloty")
    print("8. Wyjdź")

def ruletka():
    print("\n--- Ruletka ---")
    balance = 1000
    while True:
        print(f"Twój stan konta: {balance}")
        bet = int(input("Podaj kwotę zakładu (0 aby wyjść): "))
        if bet == 0:
            break
        if bet > balance:
            print("Nie masz wystarczających środków!")
            continue

        number = int(input("Podaj numer (0-36): "))
        if number < 0 or number > 36:
            print("Nieprawidłowy numer!")
            continue

        winning_number = random.randint(0, 36)
        print(f"Wylosowany numer: {winning_number}")

        if winning_number == number:
            print("Wygrałeś!")
            balance += bet * 35
        else:
            print("Przegrałeś!")
            balance -= bet

        if balance <= 0:
            print("Nie masz już pieniędzy!")
            break

def blackjack():
    print("\n--- Blackjack ---")
    balance = 1000
    while True:
        print(f"Twój stan konta: {balance}")
        bet = int(input("Podaj kwotę zakładu (0 aby wyjść): "))
        if bet == 0:
            break
        if bet > balance:
            print("Nie masz wystarczających środków!")
            continue

        player_hand = [random.randint(1, 11), random.randint(1, 11)]
        dealer_hand = [random.randint(1, 11), random.randint(1, 11)]

        print(f"Twoja ręka: {player_hand}, suma: {sum(player_hand)}")
        print(f"Ręka krupiera: [{dealer_hand[0]}, ?]")

        while sum(player_hand) < 21:
            action = input("Czy chcesz dobrać kartę (d) czy spasować (s)? ")
            if action == 'd':
                player_hand.append(random.randint(1, 11))
                print(f"Twoja ręka: {player_hand}, suma: {sum(player_hand)}")
            elif action == 's':
                break

        if sum(player_hand) > 21:
            print("Przegrałeś! Przekroczyłeś 21.")
            balance -= bet
            continue

        print(f"Ręka krupiera: {dealer_hand}, suma: {sum(dealer_hand)}")
        while sum(dealer_hand) < 17:
            dealer_hand.append(random.randint(1, 11))
            print(f"Ręka krupiera: {dealer_hand}, suma: {sum(dealer_hand)}")

        if sum(dealer_hand) > 21 or sum(player_hand) > sum(dealer_hand):
            print("Wygrałeś!")
            balance += bet
        else:
            print("Przegrałeś!")
            balance -= bet

        if balance <= 0:
            print("Nie masz już pieniędzy!")
            break

def rosyjska_ruletka():
    print("\n--- Rosyjska Ruletka ---")
    balance = 1000
    while True:
        print(f"Twój stan konta: {balance}")
        bet = int(input("Podaj kwotę zakładu (0 aby wyjść): "))
        if bet == 0:
            break
        if bet > balance:
            print("Nie masz wystarczających środków!")
            continue

        chamber = random.randint(1, 6)  # 1-6 chambers, one is empty
        print("Kręcisz bęben...")

        if chamber == 1:  # 1 is the empty chamber
            print("Pistolet nie wystrzelił! Wygrałeś!")
            balance += bet
        else:
            print("BANG! Przegrałeś!")
            balance -= bet

        if balance <= 0:
            print("Nie masz już pieniędzy!")
            break

def poker():
    print("\n--- Poker ---")
    balance = 1000
    while True:
        print(f"Twój stan konta: {balance}")
        bet = int(input("Podaj kwotę zakładu (0 aby wyjść): "))
        if bet == 0:
            break
        if bet > balance:
            print("Nie masz wystarczających środków!")
            continue

        player_hand = [random.randint(1, 13), random.randint(1, 13)]
        print(f"Twoja ręka: {player_hand}")

        # Prosta logika wygranej
        winning_hand = random.randint(1, 13)
        print(f"Wylosowana ręka: {winning_hand}")

        if max(player_hand) > winning_hand:
            print("Wygrałeś!")
            balance += bet
        else:
            print("Przegrałeś!")
            balance -= bet

        if balance <= 0:
            print("Nie masz już pieniędzy!")
            break

def kolo_krzyzyk():
    print("\n--- Kółko-krzyżyk ---")
    board = [' ' for _ in range(9)]
    current_player = 'X'
    while True:
        print_board(board)
        move = int(input(f"Gracz {current_player}, wybierz pole (1-9): ")) - 1
        if board[move] != ' ':
            print("To pole jest już zajęte!")
            continue
        board[move] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"Gratulacje! Gracz {current_player} wygrał!")
            break
        if ' ' not in board:
            print_board(board)
            print("Remis!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

def print_board(board):
    print("\n")
    for i in range(3):
        print(f"{board[i*3]} | {board[i*3+1]} | {board[i*3+2]}")
        if i < 2:
            print("---------")
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # wiersze
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # kolumny
        [0, 4, 8], [2, 4, 6]              # przekątne
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def wyscigi_konne():
    print("\n--- Wyścigi Konne ---")
    balance = 1000
    horses = ["Koń 1", "Koń 2", "Koń 3", "Koń 4"]
    while True:
        print(f"Twój stan konta: {balance}")
        bet = int(input("Podaj kwotę zakładu (0 aby wyjść): "))
        if bet == 0:
            break
        if bet > balance:
            print("Nie masz wystarczających środków!")
            continue

        print("Wybierz konia do obstawienia:")
        for i, horse in enumerate(horses, start=1):
            print(f"{i}. {horse}")
        choice = int(input("Wybierz numer konia: ")) - 1

        if choice < 0 or choice >= len(horses):
            print("Nieprawidłowy wybór!")
            continue

        winning_horse = random.choice(horses)
        print(f"Wygrał: {winning_horse}")

        if horses[choice] == winning_horse:
            print("Wygrałeś!")
            balance += bet * 2  # podwajamy stawkę
        else:
            print("Przegrałeś!")
            balance -= bet

        if balance <= 0:
            print("Nie masz już pieniędzy!")
            break

def sloty():
    print("\n--- Sloty ---")
    balance = 1000
    while True:
        print(f"Twój stan konta: {balance}")
        bet = int(input("Podaj kwotę zakładu (0 aby wyjść): "))
        if bet == 0:
            break
        if bet > balance:
            print("Nie masz wystar czających środków!")
            continue

        # Symulacja slotów
        symbols = ["🍒", "🍋", "🍊", "🍉", "🍇", "⭐"]
        spin_result = [random.choice(symbols) for _ in range(3)]
        print(f"Wynik: {' | '.join(spin_result)}")

        if spin_result[0] == spin_result[1] == spin_result[2]:
            print("Gratulacje! Wygrałeś!")
            balance += bet * 10  # wygrana 10-krotność stawki
        else:
            print("Przegrałeś!")
            balance -= bet

        if balance <= 0:
            print("Nie masz już pieniędzy!")
            break

def main():
    while True:
        print_menu()
        choice = input("Wybierz opcję: ")
        if choice == '1':
            ruletka()
        elif choice == '2':
            blackjack()
        elif choice == '3':
            rosyjska_ruletka()
        elif choice == '4':
            poker()
        elif choice == '5':
            kolo_krzyzyk()
        elif choice == '6':
            wyscigi_konne()
        elif choice == '7':
            sloty()
        elif choice == '8':
            print("Dziękujemy za grę!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()