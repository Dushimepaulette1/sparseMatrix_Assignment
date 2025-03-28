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
python main.py
```

Choose the desired operation when prompted:

1 for Addition

2 for Subtraction

3 for Multiplication

## Operations

- **Addition (1)**: Adds two sparse matrices.
- **Subtraction (2)**: Subtracts the second matrix from the first.
- **Multiplication (3)**: Multiplies two sparse matrices.

## File Paths

The script processes matrices from predefined input files:
Addition & Subtraction: easy_sample_02_1.txt and easy_sample_02_2.txt
Multiplication: easy_sample_02_1.txt and easy_sample_02_3.txt

## Changing Input Files

If you want to use different matrix files, update the file paths in main.py:

```bash
matrix_a = CompressedMatrix('path/to/your_matrix1.txt')
matrix_b = CompressedMatrix('path/to/your_matrix2.txt')
```

Alternatively, modify the script to accept file paths as command-line arguments instead of using predefined files.

## Output

The result of the operation will be displayed on the screen and saved to a file in the results directory. The output filename is generated based on the operation performed:

Addition → result_addition.txt

Subtraction → result_subtraction.txt

Multiplication → result_multiplication.txt

## Example Output

Choose an operation to perform:

1. Addition
2. Subtraction
3. Multiplication
   Enter the number of the operation (1/2/3): 1
   Saving file to : ./results/result_addition.txt

## Error Handling

If an invalid operation is chosen or an error occurs while processing the matrices, an error message will be displayed:

```bash
Error encountered: Invalid selection
```

## NB:

Ensure that the input files exist and follow the correct format before running the script.
