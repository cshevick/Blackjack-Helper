import userDecisionMaking

print("Hello, welcome to your card counter!")

# Initialize variables
num_starting_decks = int(input("\nHow many decks are you playing with: "))  # Get the number of decks being used
cards_per_deck = 52  # Standard number of cards in a deck
total_cards = num_starting_decks * cards_per_deck  # Calculate total number of cards
cards_dealt = 0  # Initialize the number of cards dealt

true_count = 0  # Initialize true count
running_count = 0  # Initialize running count
optimal_bet = 1  # Initialize optimal bet

active_status = input("Great, ready to play a hand (yes/no): ").strip().lower()  # Check if player is ready to play

def update_running_count(card, running_count):
    """Update running count based on the value of the card."""
    card = card.upper()  # Ensure card is uppercase for consistency
    if card in ["J", "Q", "K", "A", "10"]:  # High cards and Aces decrease the count
        running_count -= 1
    elif card in ["2", "3", "4", "5", "6"]:  # Low cards increase the count
        running_count += 1
    # Cards 7, 8, 9 have no effect on the running count
    return running_count

def calc_true_count(running_count, total_cards, cards_dealt):
    """Calculate the true count from the running count."""
    remaining_cards = total_cards - cards_dealt  # Calculate remaining cards
    remaining_decks = remaining_cards / cards_per_deck  # Calculate remaining decks
    if remaining_decks == 0:  # Avoid division by zero
        return 0, remaining_decks
    true_count = running_count / remaining_decks  # Calculate true count
    return round(true_count), remaining_decks

while active_status == "yes":  # Loop while player wants to continue playing
    userDecisionMaking.make_decision()  # Perform hand decision once per hand
    print("\n")

    while True:
        # Get input for each card dealt until the hand is finished
        current_card = input("Please enter the value associated with all of the cards dealt, if the hand is finished enter \"done\": ").strip().upper()
        if current_card == "DONE":  # Break loop if hand is finished
            break
        else:
            running_count = update_running_count(current_card, running_count)  # Update running count
            cards_dealt += 1  # Increment number of cards dealt

    # Calculate true count and remaining decks
    true_count, remaining_decks = calc_true_count(running_count, total_cards, cards_dealt)
    optimal_bet = max(1, true_count - 1)  # Calculate optimal bet ensuring it's at least 1

    # Print the current counts and optimal bet
    print(f"Running count: {running_count}, True count: {true_count}, Remaining decks: {remaining_decks:.2f}")
    print(f"Your optimal bet is {optimal_bet} units.")

    # Ask if the player wants to play another hand
    active_status = input("Are you playing another hand (yes/no)?: ").strip().lower()
    if active_status == "yes":
        # Ask if the decks need to be reshuffled
        reshuffle = input("Do you need to reshuffle the decks (yes/no)?: ").strip().lower()
        if reshuffle == "yes":
            cards_dealt = 0  # Reset cards dealt
            running_count = 0  # Reset running count
            print("Decks reshuffled. Starting new count.")
