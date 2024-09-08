# Advanced Calculator Application

## Overview

This application is a desktop calculator built with Python's `tkinter` library. It features both financial and scientific calculators with a glass-like user interface. Users can switch between the financial and scientific calculators using a hamburger menu.

## Features

- **Financial Calculator**: Provides basic financial operations such as Present Value (PV), Future Value (FV), Payment (PMT), and Amortization (AMT).
- **Scientific Calculator**: Supports a range of mathematical functions including square root, exponential, trigonometric functions, and more.
- **Glass-Like GUI**: Custom buttons with a glass-like appearance.
- **Hamburger Menu**: Easily switch between the financial and scientific calculators.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/advanced-calculator.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd advanced-calculator
   ```

3. **Install Required Packages:**

   Ensure you have Python 3 installed. This project uses `tkinter` which is included with Python. There are no additional packages required.

## Usage

1. **Run the Application:**

   ```bash
   python calculator.py
   ```

2. **Switch Between Calculators:**

   Use the hamburger menu on the left to toggle between the financial and scientific calculators.

## Code Structure

- **`calculator.py`**: The main script that contains the implementation of the `CalculatorApp`, `FinancialCalculator`, and `ScientificCalculator` classes.
- **`GlassButton` Class**: A custom button with a glass-like appearance.
- **`FinancialCalculator` Class**: Implements the financial calculator functionality.
- **`ScientificCalculator` Class**: Implements the scientific calculator functionality.

## Customization

- **Colors and Appearance**: Modify the color codes in the `GlassButton` class and other components to match your desired theme.
- **Calculator Functions**: Add or modify the functions and buttons as needed to fit your requirements.

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by various calculator designs.
- Built using Python's `tkinter` library for a clean and responsive GUI.
