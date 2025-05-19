import userDecisionMaking

print("Hello, welcome to your card counter!")


num_starting_decks = int(input("\nHow many decks are you playing with: ")) 
cards_per_deck = 52 
total_cards = num_starting_decks * cards_per_deck 
cards_dealt = 0 

true_count = 0 
running_count = 0 
optimal_bet = 1  

active_status = input("Great, ready to play a hand (yes/no): ").strip().lower()  

def update_running_count(card, running_count):
    """Update running count based on the value of the card."""
    card = card.upper()  
    if card in ["J", "Q", "K", "A", "10"]:  
        running_count -= 1
    elif card in ["2", "3", "4", "5", "6"]:  
        running_count += 1
  
    return running_count

def calc_true_count(running_count, total_cards, cards_dealt):
    """Calculate the true count from the running count."""
    remaining_cards = total_cards - cards_dealt 
    remaining_decks = remaining_cards / cards_per_deck  
    if remaining_decks == 0: 
        return 0, remaining_decks
    true_count = running_count / remaining_decks 
    return round(true_count), remaining_decks

while active_status == "yes": 
    userDecisionMaking.make_decision() 
    print("\n")

    while True:
        
        current_card = input("Please enter the value associated with all of the cards dealt, if the hand is finished enter \"done\": ").strip().upper()
        if current_card == "DONE":  
            break
        else:
            running_count = update_running_count(current_card, running_count)  
            cards_dealt += 1 

  
    true_count, remaining_decks = calc_true_count(running_count, total_cards, cards_dealt)
    optimal_bet = max(1, true_count - 1)  


    print(f"Running count: {running_count}, True count: {true_count}, Remaining decks: {remaining_decks:.2f}")
    print(f"Your optimal bet is {optimal_bet} units.")

  
    active_status = input("Are you playing another hand (yes/no)?: ").strip().lower()
    if active_status == "yes":
       
        reshuffle = input("Do you need to reshuffle the decks (yes/no)?: ").strip().lower()
        if reshuffle == "yes":
            cards_dealt = 0  
            running_count = 0 
            print("Decks reshuffled. Starting new count.")
