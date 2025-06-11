# Prime Number CLI

This repository provides a simple command-line interface (CLI) to check whether integers are prime, along with a suite of unit tests.

## Files

- `prime_number.py` - CLI script and module containing the `is_prime` function.
- `tests/test_prime_number.py` - Pytest-based tests for verifying `is_prime` behavior.
- `requirements.txt` - List of Python dependencies.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To check if a number is prime:

```bash
python prime_number.py 17
# Outputs: 17 is prime
```

## Testing

Run the test suite using pytest:

```bash
pytest
```
