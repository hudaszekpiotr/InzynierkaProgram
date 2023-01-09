# Modeling and Optimization of Agricultural Production

The aim of this paper was to create a program that is designed to optimize the crop schedule on a certain number of fields so as to maximize profit with limited available resources. 
For this purpose, a mathematical model was defined and the evolutionary algorithm was adapted to this specific problem.

The mathematical model allows to enter any number of types of resources, and determine how much of a given type of resource is needed at a given stage of crop cultivation. 
This resulted in a flexible model suitable for optimizing not only agricultural schedule, but also industrial one.

A Python program was created that allows user to enter model data and set algorithm parameters using a graphical interface. 
In addition, the program allows to visualize resource consumption and save or load model data from a file. In project Pandas and Qt libraries among others were used.

Computational experiments were carried out to check the influence of the parameters of the evolutionary algorithm on the obtained results.

# Instruction

## Starting the program using the .exe file

1. Download latest release
1. Open the file "mainwindow.exe" by double-clicking it

## Running the program using python

1. Install Python version 3.10.9
1. Install needed libraries (e.g. with pip):
	- PySide6 6.4
	- pandas 1.5
	- numpy 1.23
	- matplotlib 3.6.2
	- distinctip 1.2
1. Run the program using the command
    ```bash
    python mainwindow.py
    ```
   
## Loading model data

The "numerical_tests" folder contains sample data for crop types, fields, and resources.
You can load this data using the "load data" button in the program.
