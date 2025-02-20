# Sparse Matrix

## Overview

The Sparse Matrix project provides a Python implementation of a memory-efficient sparse matrix class, allowing users to perform basic matrix operations such as addition, subtraction, and multiplication. Sparse matrices are particularly useful when dealing with large datasets where most elements are zero, enabling efficient storage and computation.

## Features

- Load sparse matrices from text files
- Perform addition, subtraction, and multiplication of sparse matrices
- Save the result of operations to a text file

## Setup

To run this project, ensure you have Python 3 installed on your machine. Clone the repository and navigate to the project directory:

```bash
git clone <repository_url>
cd sparseMatrix_Assignment
```

## Usage

1. Prepare your sparse matrix files in the `sample_inputs` directory. Each file should follow the format:

```
rows=<number_of_rows>
cols=<number_of_columns>
(row1, col1, value1)
(row2, col2, value2)
...
```

2. Run the main script with two matrix files as arguments. For example, to add two matrices:

```bash
python main.py sample_inputs/matrixfile1.txt sample_inputs/matrixfile2.txt
```

3. Choose the desired operation (addition, subtraction, or multiplication) when prompted.

## Operations

- **Addition (1)**: Adds two sparse matrices.
- **Subtraction (2)**: Subtracts the second matrix from the first.
- **Multiplication (3)**: Multiplies two sparse matrices.

## Output

The result of the operation will be displayed on the screen
