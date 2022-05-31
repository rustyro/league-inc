from typing import List, Tuple, Union

from app import app
from .constants import CORRUPT_FILE_ERR, INVALID_FILE_ERR, NO_FILE_ERR, NON_SQUARE_ERR, BLANK_FILE_ERR, NON_INT_ERR
from .transformer import Transformer
from flask import request
from werkzeug.utils import secure_filename
from werkzeug import exceptions
import csv
import os


ALLOWED_EXTENSIONS = ['csv']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def validate_content(
        matrix: Union[List[List[str]], List[str]],
        row_only: bool = False,
        row_length: int = None
) -> Tuple[bool, Union[str, None]]:
    """
    Validated that the content of the matrix meets the following requirements:
    - It's not an empty array i.e. the CSV file contains values
    - It must be a square matrix according to the spec
    - Value of each matrix coordiante must be an integer
    :param matrix:
    :param row_only:
    :param row_length:
    :return:
    """
    valid = True
    error = None
    # check the only integer constraint
    if row_only:
        for idx in matrix:
            valid = idx.isdigit()
            if not valid:
                error = NON_INT_ERR
                break
    # check the non-empty and square constraint
    # NOTE: If the value is a scalar it's considered to be a 1x1 square matrix
    else:
        if not matrix:
            valid = False
            error = BLANK_FILE_ERR
        elif not matrix[0]:
            valid = False
            error = BLANK_FILE_ERR
        elif len(matrix) != len(matrix[0]):
            valid = False
            error = f"{NON_SQUARE_ERR}, got {len(matrix)} X {len(matrix[0])}"
    if not valid:
        raise exceptions.BadRequest(error)
    return valid, error


def process_request():
    """

    :return:
    """

    matrix = []
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            raise exceptions.BadRequest(NO_FILE_ERR)

        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '' or not allowed_file(file.filename):
            raise exceptions.BadRequest(INVALID_FILE_ERR)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            with open(filepath, newline='') as csvfile:
                try:
                    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                    for row in reader:
                        value = row[0].strip().split(',') if row else []
                        validate_content(value, row_only=True)
                        matrix.append(value)
                except UnicodeDecodeError as e:
                    raise exceptions.BadRequest(CORRUPT_FILE_ERR)
        validate_content(matrix)
        return matrix


@app.route('/echo', methods=["POST"])
def echo() -> str:
    """ The Echo endpoint """

    return Transformer.echo(process_request())


@app.route('/invert', methods=["POST"])
def invert() -> str:

    return Transformer.invert(process_request())


@app.route('/flatten', methods=["POST"])
def flatten() -> str:

    return Transformer.flatten(process_request())


@app.route('/sum', methods=["POST"])
def add() -> str:

    return Transformer.add(process_request())


@app.route('/multiply', methods=["POST"])
def multiply() -> str:

    return Transformer.multiply(process_request())

