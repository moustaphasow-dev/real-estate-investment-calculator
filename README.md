# Real Estate Investment Calculator

A Python project that analyzes rental property deals using common real estate investment metrics.

## Features

- Calculates Net Operating Income (NOI)
- Calculates annual cash flow
- Calculates cap rate
- Calculates cash-on-cash return
- Calculates Debt Service Coverage Ratio (DSCR)
- Gives a YES or NO investment decision based on set criteria

## Example Output

```text
==== DEAL REPORT ====

NOI: $12,415.68
Annual cash flow: -$799.47
Cap rate: 5.9%
CoC return: -1.4%
DSCR: 0.9

==== IS PROPERTY A YES OR NO? ====
NO
```

## Built With

- Python

## What I Learned

- Functions
- Dictionaries
- Conditional statements
- Financial calculations
- Formatting program output
- Debugging
- Git and GitHub version control

## Future Improvements

- Allow users to enter their own property data
- Analyze multiple properties
- Add more real estate investment metrics
- Add input validation and error handling
- Build a graphical or web interface

## How to Run

1. Make sure Python 3 is installed.
2. Clone this repository.
3. Open the project folder in a terminal.
4. Run:

```bash
python3 real_estate_calculator.py
```

## Deal Criteria

The calculator currently marks a property as a YES when all of the following conditions are met:

- Cash-on-cash return is at least 12%
- DSCR is at least 1.2
- Cap rate is at least 7%
