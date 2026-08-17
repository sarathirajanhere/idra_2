# Number Guessing Game 🎯

An interactive command-line game where players guess a randomly generated number within a custom range. Features three difficulty levels that dynamically adjust allowed attempts based on range size.

## Features

- **Custom Range**: Player defines lower and upper bounds
- **Three Difficulties**:
  - **Easy**: Max attempts = range size (or 10 minimum)
  - **Medium**: Max attempts = half range size (or 7 minimum)
  - **Hard**: Max attempts = quarter range size (or 5 minimum)
- **Input Validation**: Handles non-integer inputs gracefully
- **Replay Loop**: Play multiple rounds without restarting
- **Helpful Feedback**: "Too high"/"Too low" hints with remaining attempts

## Tech Stack

- **Language**: Python 3.x
- **Dependencies**: `random` (stdlib)

## Installation

```bash
git clone https://github.com/sarathirajanhere/idra_2.git
cd idra_2
```

## Usage

```bash
python guess_the_number.py
```

### Example Session

```
==========================================
NUMBER GUESSING GAME 
==========================================
Enter the lower bound: 1
Enter the upper bound: 100

Select difficulty:
  1) Easy
  2) Medium
  3) Hard
Enter 1, 2, or 3: 2

I'm thinking of a number between 1 and 100.
You have 7 attempt(s). Good luck!

Enter your guess (1–100): 50
Too low!  (Attempts left: 6)

Enter your guess (1–100): 75
Too high! (Attempts left: 5)
...
Correct! You got it in 4 attempt(s).

Play again? (y/n): n
Thanks for playing!
```

## File Structure

```
idra_2/
├── guess_the_number.py    # Main game logic
└── README.md              # This file
```

## Key Concepts Demonstrated

- `random.randint()` for random number generation
- Function decomposition (`get_range`, `get_max_attempts`, `get_guess`, `play`, `main`)
- Input validation with `try/except`
- Loop control with `while` and `for`
- Conditional logic and user interaction

---

*Part of the IDRA learning series — simple, focused Python projects for beginners.*
