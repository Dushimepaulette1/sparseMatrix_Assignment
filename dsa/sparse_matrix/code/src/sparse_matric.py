#!/usr/bin/env python3
"""
SparseMatrix Class: Handles operations on large, memory-efficient matrices.
"""

class SparseMatrix:
    def __init__(self, numRows=0, numCols=0):
        """
        Initialize a sparse matrix.
        - numRows: Number of rows
        - numCols: Number of columns
        """
        self.matrix = {}
        self.numRows = numRows
        self.numCols = numCols

    @staticmethod
    def load(matrixFilePath):
        """
        Load a sparse matrix from a file.
        - matrixFilePath: Path to the file containing matrix data.
        Returns: SparseMatrix object
        """
        try:
            with open(matrixFilePath, 'r') as file:
                lines = file.readlines()
                numRows = int(lines[0].strip().split('=')[1])
                numCols = int(lines[1].strip().split('=')[1])
                matrix = SparseMatrix(numRows, numCols)

                for line in lines[2:]:
                    if line.strip():
                        row, col, val = map(int, line.strip()[1:-1].split(','))
                        matrix.setElement(row, col, val)

                return matrix
        except Exception as e:
            raise ValueError("Input file has wrong format") from e

    def getElement(self, row, col):
        """
        Get an element from the sparse matrix.
        """
        return self.matrix.get((row, col), 0)

    def setElement(self, row, col, value):
        """
        Set an element in the sparse matrix.
        If value is 0, remove the entry to save memory.
        """
        if value != 0:
            self.matrix[(row, col)] = value
        elif (row, col) in self.matrix:
            del self.matrix[(row, col)]

    def __add__(self, other):
        """
        Add two sparse matrices.
        Returns: New SparseMatrix object
        """
        if not isinstance(other, SparseMatrix):
            raise ValueError("Matrices can only be added to matrices")
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions must match for addition")

        result = SparseMatrix(self.numRows, self.numCols)
        for (row, col), value in self.matrix.items():
            result.setElement(row, col, value + other.getElement(row, col))
        for (row, col), value in other.matrix.items():
            if (row, col) not in self.matrix:
                result.setElement(row, col, value)
        return result

    def __sub__(self, other):
        """
        Subtract two sparse matrices.
        Returns: New SparseMatrix object
        """
        if not isinstance(other, SparseMatrix):
            raise ValueError("Matrices can only be subtracted from matrices")
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions must match for subtraction")

        result = SparseMatrix(self.numRows, self.numCols)
        for (row, col), value in self.matrix.items():
            result.setElement(row, col, value - other.getElement(row, col))
        for (row, col), value in other.matrix.items():
            if (row, col) not in self.matrix:
                result.setElement(row, col, -value)
        return result

    def __mul__(self, other):
        """
        Multiply two sparse matrices.
        Returns: New SparseMatrix object
        """
        if not isinstance(other, SparseMatrix):
            raise ValueError("Matrices can only be multiplied to matrices")
        if self.numCols != other.numRows:
            raise ValueError("Matrix multiplication requires columns of A == rows of B")

        result = SparseMatrix(self.numRows, other.numCols)
        for (row, col), value in self.matrix.items():
            for k in range(other.numCols):
                if (col, k) in other.matrix:
                    result.setElement(row, k, result.getElement(row, k) + value * other.getElement(col, k))
        return result

    def __str__(self):
        """
        Convert matrix to string format.
        """
        result = f"rows={self.numRows}\ncols={self.numCols}\n"
        for (row, col), value in sorted(self.matrix.items()):
            result += f"({row}, {col}, {value})\n"
        return result

    def to_file(self, file_path):
        """
        Write matrix to a file.
        """
        with open(file_path, 'w') as file:
            file.write(str(self))
