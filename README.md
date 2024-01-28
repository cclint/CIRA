
# Basic OOP in Python and Using Sphinx for Documentation

## Python Object-Oriented Programming (OOP) Script

This Python script (`src/oop.py`) demonstrates a basic implementation of an adder using object-oriented programming (OOP) principles. It includes a class `Adder` with methods to initialize the object, add values, and provide string representations.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/cclint/CIRA.git
   cd CIRA
   ```

2. **Run the Script:**
   ```bash
   python oop.py
   ```

   This script creates an instance of the `Adder` class, adds values, and prints the object's state.

## Class Methods

- `__init__(self, value=0)`: Initializes an instance of the Adder class.
- `__repr__(self)`: Returns a string representation for debugging.
- `__str__(self)`: Returns a human-readable string representation.
- `add(self, num)`: Adds the specified number to the current value.

## Sphinx Documentation

To generate documentation using Sphinx, follow these steps:

1. **Install Sphinx:**
   ```bash
   pip install sphinx
   ```

2. **Navigate to the `docs` directory:**
   ```bash
   cd docs
   ```

3. **Initialize Sphinx:**
   ```bash
   sphinx-quickstart
   ```

4. **Build HTML Documentation:**
   ```bash
   make html
   ```
5. **View HTML in Firefox:**
   ```bash
   firefox index.html
   ```
6. **View HTML Documentation:**
   Open the generated HTML documentation in a web browser. The HTML files should be located in the `_build/html` directory within the `docs` directory.


## Prerequisites

- [Firefox](https://www.mozilla.org/en-US/firefox/new/): Install Firefox to view the generated HTML file.

## Result (HTML files rendered in FireFox)
![adder1](https://github.com/cclint/CIRA/assets/45945445/a29a92a8-0bc1-4ea1-9d3d-a371340cee2f)
![adder2](https://github.com/cclint/CIRA/assets/45945445/56320523-fb16-4f64-a9af-e8a730efb87f)



```
