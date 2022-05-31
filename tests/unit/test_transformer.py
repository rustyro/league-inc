from app.transformer import Transformer


class TestTransformer:
    """
    Test the transformer class function by function
    """

    def test_echo(self):
        """
        test the echo function
        :return:
        """
        assert Transformer.echo([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]) == '1,2,3\n4,5,6\n7,8,9'
        
    def test_invert(self):
        """
        test the invert function
        :return:
        """
        assert Transformer.invert([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]) == '1,4,7\n2,5,8\n3,6,9'
        #  test multi digit numbers
        assert Transformer.invert([["1", "222", "3"], ["4", "5", "96"], ["7", "8", "9"]]) == '1,4,7\n222,5,8\n3,96,9'

    def test_flatten(self):
        """
        test the flatten function
        :return:
        """
        assert Transformer.flatten([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]) == '1,2,3,4,5,6,7,8,9'
    
    def test_sum(self):
        """
        test the add function
        :return:
        """
        assert Transformer.add([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]) == '45'

    def test_multiply(self):
        """
        test the multiply function
        :return:
        """
        assert Transformer.multiply([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]) == '362880'
