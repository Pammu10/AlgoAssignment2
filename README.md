# AlgoAssignment2

This project contains C++ implementations of algorithms and Python scripts for data generation, analysis, and visualization.  
The setup is tested and works on **Windows 11** only.  

---

### Prerequisites
- Windows 11  
- C++ (g++ compiler)  
- Python (with `uv` installed)  

---

### Getting Started

1. **Clone the repository**
```
git clone https://github.com/Pammu10/AlgoAssignment2.git
cd AlgoAssignment2
  ```



2. **Compile the C++ code**
- To compile all algorithms:
  ```
  make
  ```
- To compile the input generator:
  ```
  g++ generate_inputs.cpp -o generate_inputs
  ```
- Run the generator:
  ```
  .\generate_inputs
  ```
This will create input files inside the **input** folder.

3. **Set up Python environment**
- Install `uv` (if not already installed):
  ```
  pip install uv
  ```
- Initialize and install dependencies:
  ```
  uv init .
  uv add matplotlib pandas
  ```

---


### Running all the algorithms

uv run run_all.py

### Running the Assignment Scripts

- **Question 3**
uv run question3.py

- **Question 4**
uv run question4.py

- **Question 5**
uv run question5.py


Running these scripts will generate required data and graphs in the output.

---
