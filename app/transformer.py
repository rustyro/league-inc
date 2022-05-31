"""
transformers.py
Contains a Transformer class object that has useful methods to manipulate matrices
"""

from typing import List


class Transformer:
    """
    Transformer class with useful methods to manipulate square matrices.
    To maintain efficiency functions in this class DO NOT support integer datatypes as values for a matrix index,
    given that values from the CSV file uploaded will always be of type string.
    If used the functions will always raise an error
    """

    @classmethod
    def echo(cls, matrix: List[List[str]]) -> str:
        """
        Read and return a string matrix without performing any transformation
        :param matrix: an array of comma separated integer strings
        :return: string matrix
        """
        matrix = [','.join(i) for i in matrix]
        res = "\n".join(matrix)
        return res

    @classmethod
    def invert(cls, matrix: List[List[str]]) -> str:
        """
        Transpose the given matrix vertically.
        E.G: 1,2,3      1,4,7
             4,5,6  =>  2,5,8
             7,8,9      3,6,9

        :param matrix: an array of comma separated integer strings
        :return: Inverted matrix
        """
        rows = len(matrix)
        columns = len(matrix[0])

        res = None
        for j in range(columns):
            row = None
            for i in range(rows):
                row = matrix[i][j] if not row else f"{row},{matrix[i][j]}"

            res = f"{row}" if not res else f"{res}\n{row}"

        return res

    @classmethod
    def flatten(cls, matrix: List[List[str]]) -> str:
        """
        Return the matrix as a 1 line string, with values separated by commas
        :param matrix: an array of comma separated integer strings
        :return:
        """
        matrix = [','.join(i) for i in matrix]
        return ",".join(matrix)

    @classmethod
    def add(cls, matrix: List[List[str]]) -> str:
        """
        Determine the sum of the integers in the matrix
        :param matrix: an array of comma separated integer strings
        :return: string integer of sum
        """

        # make an array of string integers
        numbers = cls.flatten(matrix).split(",")

        return str(sum([int(i) for i in numbers]))

    @classmethod
    def multiply(cls, matrix: List[List[str]]) -> str:
        """
        Determine the product of the integers in the matrix
        :param matrix: an array of comma separated integer strings
        :return: string integer of matrix product
        """
        # make an array of string integers
        numbers = cls.flatten(matrix).split(",")
        product = 1
        for i in numbers:
            product = product * int(i)
        return str(product)
