# Advent of Code 2025

This project contains my solutions for Advent of Code 2025 in Python.

## Setup

1. Activate the virtual environment:
   ```bash
   source .venv/Scripts/activate
   ```

2. Install dependencies (already done):
   ```bash
   pip install pytest
   ```

## Running Solutions

Run a specific day's solution:
```bash
python day01.py
```

## Testing

Run all tests:
```bash
pytest
```

Run tests for a specific day:
```bash
pytest test_day01.py
```

Run tests in verbose mode:
```bash
pytest -v
```

## Project Structure

- `dayXX.py` - Solution code for each day
- `test_dayXX.py` - Unit tests for each day
- `dayXX_input.txt` - Puzzle input (not tracked in git)
