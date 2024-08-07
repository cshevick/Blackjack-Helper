# Card Counter and Blackjack Decision-Making Application

This project is a Python-based application designed to help users count cards and make optimal decisions while playing blackjack. The application features a card counter that updates running and true counts and provides betting advice based on the true count. It also includes a decision-making module that guides users on the best actions to take based on their hand and the dealer's up card.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Contributing](#contributing)
- [License](#license)

## Overview

This application helps blackjack players by providing two main functionalities:
1. **Card Counting:** Keeps track of the running and true counts and suggests optimal betting strategies.
2. **Decision Making:** Uses a pre-loaded strategy chart to recommend the best action (Hit, Stand, Double Down, Split) based on the player's hand and the dealer's up card.

## Features

- **Card Counter:**
  - Updates running count based on cards dealt.
  - Calculates the true count based on the remaining cards in the deck.
  - Suggests the optimal bet based on the true count.

- **Decision Making:**
  - Uses a strategy chart loaded from a CSV file.
  - Recommends actions based on the player's hand and dealer's up card.
  - Handles special cases such as pairs and soft hands.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/card-counter.git
   cd card-counter
