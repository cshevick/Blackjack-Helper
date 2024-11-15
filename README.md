# Blackjack Helper

This project is a Python-based application designed to help users count cards by keeping track of the running and true count and giving users optimal betting units based on those values. The application then gives users optimal decisions by extracting decisions from a blackjack strategy sheet CSV.

## Installation
  1. Clone the repository in IDE of choice using: https://github.com/cshevick/Blackjack-Helper.git
  2. Install the required dependencies: pip install pandas

## Usage

This application helps blackjack players by providing two main functionalities:
1. **Card Counting:** Keeps track of the running and true counts and suggests optimal betting strategies.
2. **Decision Making:** Uses a pre-loaded strategy chart to recommend the best action (Hit, Stand, Double Down, Split) based on the player's hand and the dealer's up card.

## Gameplay Instructions
This application is created to be played alongside a real-life blackjack game so that the user can see which cards are played. 

1. **Deck Setup**:
   - At the start of the game, you’ll be prompted to enter the number of decks you are using (e.g., 1, 2, or 6 decks). This will help calculate running and true counts during gameplay.

2. **Playing a Hand**:
   - You’ll be asked for the dealer’s visible card and your two initial cards. The application will calculate the initial hand value and suggest an action based on the strategy data in `blackjackBook.csv`.

   - **Recommended Actions**:
     - The app will suggest actions like `Hit`, `Stand`, `Double Down`, or `Split` based on your hand value and the dealer’s card.
     - Follow the recommendations and proceed based on the advice given. If you draw a new card, you’ll be asked to input its value.

3. **Card Counting**:
   - After each hand, enter each card dealt until the hand is complete by typing in their values (e.g., `2`, `10`, `A`).
   - To calculate the running and true counts, enter each card until you type `"DONE"` to end that hand.
   - The app will update and display:
     - **Running Count**: The total count based on the Hi-Lo counting system.
     - **True Count**: Calculated by dividing the running count by the remaining decks.
     - **Optimal Bet**: Suggested bet units based on the true count.

4. **Continuing or Reshuffling**:
   - After each hand, you can choose to:
     - Play another hand by typing `"yes"`.
     - Reshuffle the decks if needed, which resets the running and true counts.

5. **Ending the Game**:
   - Type `"no"` when asked if you want to play another hand to end the session.

### Example Workflow

1. Enter the number of decks (e.g., `6`).
2. Input the dealer’s visible card and your two initial cards.
3. Follow the recommended action (`Hit`, `Stand`, etc.).
4. Enter each card dealt after the hand until typing `"DONE"`.
5. View your current running count, true count, and optimal bet.
6. Decide to play another hand or end the game.

## License
This project is licensed under the MIT License. Feel free to modify and use the code as per your needs.

