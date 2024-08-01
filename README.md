# String Calculator TDD Kata


This project implements a string calculator based on the TDD (Test-Driven Development) approach. The add function takes a string of comma-separated numbers (or with custom delimiters) and returns their sum. It also handles various delimiters and raises exceptions for negative numbers.


## Features

- Empty String: Returns 0.
- Single Number: Returns the number itself.
- Comma-Separated Numbers: Sums the numbers separated by commas.
- New Lines: Handles new lines as delimiters in addition to commas.
- Custom Delimiters: Allows specification of custom delimiters using the format //[delimiter]\n[numbers...].
- Negative Numbers: Raises an exception if negative numbers are present, including all negative numbers in the error message.


## Testing

The project includes test cases to validate the add function, ensuring it handles different inputs and scenarios correctly.

To run the tests, use the following command:

```bash
  python test_calculator.py
```