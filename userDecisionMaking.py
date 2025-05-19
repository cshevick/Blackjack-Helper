import pandas as pd

csv_file_path = "blackjackBook.csv"


df = pd.read_csv(csv_file_path, dtype={'Hand': str})


action_map = {
    'H': 'Hit',
    'D': 'Double Down',
    'S': 'Stand',
    'SP': 'Split'  
}

def calculate_hand_value(hand):
    """Calculate the best value for the hand considering Aces can be 1 or 11."""
    values = [0]
    card_values = {'J': 10, 'Q': 10, 'K': 10, 'A': 1} 

    for card in hand:
        if card == 'A':
            new_values = []
            for value in values:
                new_values.append(value + 1)
                new_values.append(value + 11)
            values = new_values
        elif card in card_values:
            card_value = card_values[card]
            new_values = []
            for value in values:
                new_values.append(value + card_value)
            values = new_values
        else:
            try:
                card_value = int(card)
            except ValueError:
                print(f"Invalid card value: {card}")
                return -1  
            new_values = []
            for value in values:
                new_values.append(value + card_value)
            values = new_values

    valid_values = [value for value in values if value <= 21]
    return max(valid_values) if valid_values else min(values)

def make_decision():
    def play_hand(hand):
        hand_value = calculate_hand_value(hand)
        if hand_value == -1:
            return  

        print(f"Initial hand value: {hand_value}")
        action = 'H'

        while action != 'S':
          
            if dealer_card not in df.columns:
                print(f"Dealer card '{dealer_card}' is not a valid column in the DataFrame.")
                return
            if not any(df['Hand'] == str(hand_value)):
                print(f"Hand value '{hand_value}' is not a valid row in the DataFrame.")
                return

         
            action_series = df.loc[df['Hand'] == str(hand_value), dealer_card]
            if action_series.empty:
                print(f"No action found for hand value '{hand_value}' and dealer card '{dealer_card}'.")
                return

            action = action_series.values[0]
            action_word = action_map.get(action, 'Unknown')
            print("Your recommended action is to " + action_word)

            if action_word == 'Unknown':
                print("The action retrieved is not recognized. Exiting.")
                return

            if action == 'H':
                added_card = input("What card did you receive?: ").strip().upper()
                hand.append(added_card)
                hand_value = calculate_hand_value(hand)
                if hand_value == -1:
                    return  
                print("Your new sum is " + str(hand_value))
                if hand_value > 21:
                    print("Sorry, you busted.")
                    break
            elif action == 'D':
                added_card = input("What card did you receive?: ").strip().upper()
                hand.append(added_card)
                hand_value = calculate_hand_value(hand)
                if hand_value == -1:
                    return  
                print("Your new sum is " + str(hand_value))
                if hand_value > 21:
                    print("Sorry, you busted.")
                break
            elif action == 'SP':
                print("You chose to split.")
                return 'SP'

    dealer_card = input("\nWhat card is the dealer showing? ").strip().upper()
    dealer_card = dealer_card if dealer_card not in ['J', 'Q', 'K'] else '10'

    hand = input("What are your two initial cards? (separated by a space) ").strip().upper().split()

    if len(hand) != 2:
        print("Invalid number of cards. Please enter exactly two cards.")
        return

    if hand[0] == hand[1]:
        print("You have a pair and can choose to split.")
        split_choice = input("Do you want to split? (yes/no) ").strip().lower()
        if split_choice == 'yes':
            hand1 = [hand[0]]
            hand2 = [hand[1]]
            print("Playing first hand:")
            result1 = play_hand(hand1)
            if result1 != 'SP':
                print("Playing second hand:")
                play_hand(hand2)
            return

    play_hand(hand)
