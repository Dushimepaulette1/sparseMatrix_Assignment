#!/usr/bin/env python3
"""
Main script to perform operations on sparse matrices.
"""

import sys
from sparse_matrix import SparseMatrix

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <matrix1_path> <matrix2_path>")
        return

    matrix1_path = sys.argv[1]
    matrix2_path = sys.argv[2]

    matrix1 = SparseMatrix.load(matrix1_path)
    matrix2 = SparseMatrix.load(matrix2_path)
    print("Matrix 1 dimensions:", matrix1.numRows, "x", matrix1.numCols)
    print("Matrix 2 dimensions:", matrix2.numRows, "x", matrix2.numCols)

    print("Choose an operation to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")

    operation = input("Enter the number of the operation (1/2/3): ")

    if operation in ["1", "2"]:
        # Addition or Subtraction
        if matrix1.numRows != matrix2.numRows or matrix1.numCols != matrix2.numCols:
            print("Error: Matrices must have the same dimensions for addition/subtraction.")
            return

    if operation == '1':
        result = matrix1 + matrix2
    elif operation == '2':
        result = matrix1 - matrix2
    elif operation == '3':
        # Check dimensions for multiplication
        if matrix1.numCols != matrix2.numRows:
            print("Error: For multiplication, Matrix 1's columns must match Matrix 2's rows.")
            return
        result = matrix1 * matrix2
    else:
        print("Unknown operation. Please enter 1, 2, or 3.")
        return

    result.to_file("results.txt")
    print("The result has been written to results.txt")

if __name__ == "__main__":
    main()
