Adder Python Script
===================

This Python script demonstrates a basic implementation of an adder using object-oriented programming (OOP) with the following features:

- ``__init__``: Initialization method to set the initial value of the adder.
- ``__repr__``: String representation method for debugging purposes.
- ``__str__``: Human-readable string representation method.
- ``add``: Method to add a specified number to the adder's value.

How to Run
----------

1. Install python if you haven't already

2. Clone this repo: https://github.com/cclint/CIRA.git

3. Open a terminal or command prompt and navigate to the directory where the script (`oop.py`) is located.

4. Run the script using the following command:

   .. code-block:: bash

      python oop.py

Overview of Methods in oop.py
-------------------

``__init__(self, value=0)``
   This method initializes an instance of the Adder class and sets the default value variable to 0 of type int. 

   - ``value``: Again, sets the initial value of the adder (default is 0).

``__repr__(self)``
   This returns a string representation of the Adder object.

   Used for debugging purposes.

``__str__(self)``
   Returns a more human readable string representation of the Adder object.

   Used when the object is printed using the ``print`` function. So, if a print(obj), we will get the value of self.value. 

``add(self, num)``
   Adds the specified number (``num``) to the current value of the Adder object.

   Returns the updated value after the addition.

Example Usage
-------------

.. code-block:: python

   # Create an instance of the Adder class
   my_adder = Adder()

   # prints initial state
   print("Initial state:")
   print(my_adder)

   # adds 5 to the adder (should equal 5)
   my_adder.add(5)
   print("\nAdding 5:")
   print(my_adder)

   # adds 10 to the adder (should equal 15)
   my_adder.add(10)
   print("\nAdding 10:")
   print(my_adder)

   # prints the representation of the Adder object
   print("\nRepresentation of the Adder object:")
   print(repr(my_adder))

