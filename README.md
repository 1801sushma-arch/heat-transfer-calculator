# heat-transfer-calculator
A python based heat transfer calculator with CSV data storage and Matplotlib visualization

Heat Transfer Calculator

About the Project

I'm a mechanical engineering student learning Python, and I wanted to try something different from just practising coding exercises.
So, I built this Heat Transfer Calculator to connect what I learn in mechanical engineering with programming.

The program calculates the heat transfer rate through a wall at different thicknesses while keeping the other parameters constant. It also saves the results and plots a graph to help visualize how wall thickness affects heat transfer.

The Engineering Behind It
The project is based on the one-dimensional steady-state heat conduction equation:
[Q=(kA(T₁-T₂)/L]

Where:

- Q – Heat transfer rate (W)
- k – Thermal conductivity (W/m·K)
- A – Wall area (m²)
- T₁ – Inside temperature
- T₂ – Outside temperature
- L – Wall thickness (m)

What Can This Program Do?

- Accepts engineering inputs from the user.
- Checks inputs for basic errors.
- Generates multiple wall thickness values.
- Calculates the heat transfer rate for each thickness.
- Stores the calculated results in a CSV file.
- Reads the saved data back into Python.
- Plots a graph using Matplotlib to visualize the results.

Tools and Technologies

- Python
- Matplotlib
- CSV file handling

Getting Started

First, install the required library:

pip install -r requirements.txt

Run the program:

python heat_transfer_calculator.py

What I Learned
While building this project, I got to practise:

- Functions, parameters and return values
- Conditional statements and loops
- Lists and tuples
- Input validation and exception handling
- File handling and CSV operations
- Reading, storing and retrieving data
- Data visualization using Matplotlib

More importantly, I learned how programming concepts can be applied to solve problems related to mechanical engineering.

What's Next?
This is one of my first steps towards combining mechanical engineering with programming. I look forward to improving this project and building more engineering-based Python applications.

Note: This is an educational project based on a simplified heat conduction model, not a validated engineering simulation tool.
