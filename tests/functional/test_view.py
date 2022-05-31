"""
test_view.py
Test the view endpoints
"""
import os
from app import constants


def upload(url: str, client, get_file, filename="valid.csv", expected_status_code=200):
    """
    Helper to handle the upload making the http call
    :param url: Transformation endpoint
    :param client: Test client
    :param get_file: file fetcher fixture
    :param filename: name of the file to fetch
    :param expected_status_code: expected http response status code for the request
    :return: Response
    """
    here_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fixture_dir = os.path.join(here_dir, '../../fixtures')
    data = dict(file=get_file(f"{fixture_dir}/{filename}"))
    res = client.post(url, data=data, content_type='multipart/form-data')
    assert res.status_code == expected_status_code

    return res


class TestView:

    def test_echo(self, client, get_file):
        """ Test the echo endpoint """
        res = upload("/echo", client, get_file)
        assert res.text == '1,2,3\n4,5,6\n7,8,9'

    def test_invert(self, client, get_file):
        """ Test the invert endpoint """
        res = upload("/invert", client, get_file)
        assert res.text == '1,4,7\n2,5,8\n3,6,9'

    def test_flatten(self, client, get_file):
        """ Test the 'flatten' endpoint"""
        res = upload("/flatten", client, get_file)
        assert res.text == '1,2,3,4,5,6,7,8,9'

    def test_flatten_non_single_digit(self, client, get_file):
        """ Test multi digit numbers behave as expected"""
        res = upload("/flatten", client, get_file, filename="valid-multiple.csv")
        assert res.text == '1,2,13,4,555,6,7,8,9000'

    def test_sum(self, client, get_file):
        """ Test the summation endpoint """
        res = upload("/sum", client, get_file)
        assert res.text == "45"
    
    def test_multiply(self, client, get_file):
        """ Test the product endpoint """
        res = upload("/multiply", client, get_file)
        assert res.text == '362880'


class TestErrorHandling:

    def test_blank_file(self, client, get_file):
        """ Test that a blank csv file with no data is handeled"""
        res = upload("/echo", client, get_file, "blank.csv", 400)
        assert res.text.split(":")[-1].strip() == constants.BLANK_FILE_ERR

    def test_wrong_file_format(self, client, get_file):
        """ Test that only CSV files are accepted"""
        res = upload("/echo", client, get_file, "blank.txt", 400)
        assert res.text.split(":")[-1].strip() == constants.INVALID_FILE_ERR

    def test_corrupt_file(self, client, get_file):
        """ Test that error due to corrupt CSV file is handeled"""
        res = upload("/echo", client, get_file, "corrupt.csv", 400)
        assert res.text.split(":")[-1].strip() == constants.CORRUPT_FILE_ERR

    def test_non_square_matrix(self, client, get_file):
        """ Validate that Non-square matrices are not accepted"""
        res = upload("/echo", client, get_file, "non-square.csv", 400)
        assert constants.NON_SQUARE_ERR in res.text.split(":")[-1].strip()

    def test_non_integer_input(self, client, get_file):
        """ Test that only matrices with integer inputs will be allowed"""
        res = upload("/echo", client, get_file, "non-int.csv", 400)
        assert res.text.split(":")[-1].strip() == constants.NON_INT_ERR

    def test_no_file(self, client, get_file):
        """ Test validation on absent file """
        res = client.post("/echo", data={}, content_type='multipart/form-data')
        assert res.status_code == 400
        assert res.text.split(":")[-1].strip() == constants.NO_FILE_ERR
