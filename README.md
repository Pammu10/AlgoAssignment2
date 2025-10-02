Here is the entire content for your README.md file inside a single code block. Just click the "Copy" button in the top-right corner of the block and paste it directly into your README.md file on GitHub or in any text editor.

Markdown

# AlgoAssignment2

This repository contains the source code and scripts for an algorithm assignment. The project involves compiling and running C++ programs to generate data, and then using Python scripts to process this data and generate graphs.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

* **Operating System:** Windows 11 (This code has only been tested on Windows 11).
* **Git:** For cloning the repository.
* **C++ Compiler:** A C++ compiler and the `make` utility (like the one provided by MinGW or MSYS2).
* **Python:** A recent version of Python.
* **uv:** A Python packaging tool.

## Setup and Installation

Follow these steps to set up the project on your local machine.

### 1. Get the Code

Clone the repository from GitHub using the following command:
```bash
git clone [https://github.com/Pammu10/AlgoAssignment2.git](https://github.com/Pammu10/AlgoAssignment2.git)
2. Navigate to the Directory
Go into the directory that you just cloned:

Bash

cd AlgoAssignment2
3. Compile the C++ Code
Once inside the directory, compile the C++ source files.

Compile all algorithm implementations:

Bash

make
Compile the input generator:

Bash

g++ generate_inputs.cpp -o generate_inputs
4. Generate Input Data
Run the compiled input generator to create the necessary files in the input/ folder.

Bash

.\generate_inputs.exe
5. Set Up the Python Environment
Next, set up the Python environment using uv to install the required packages.

Initialize a new virtual environment:

Bash

uv init .
Install the necessary Python libraries (matplotlib and pandas):

Bash

uv add matplotlib pandas
Your Python environment is now ready.

How to Run
After completing the setup, you can run the Python scripts for each specific question in the assignment.

For Question 3
Bash

uv run python question3.py
For Question 4
Bash

uv run python question4.py
For Question 5
Bash

uv run python question5.py
Running these scripts will execute the compiled C++ programs with the generated inputs and produce all the necessary data and graphs as output.