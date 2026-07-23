"""
Class file for input-output pair objects.
"""

class IOPair:
    """
    Class for easily defining input-output pairs.

    Attributes
    ----------
    input_tuple : tuple | any
        Input tuple for the input-output pair.
    output_tuple : tuple | any
        Output tuple for the output-input pair.

    """
    def __init__(self, input_tuple=(), output_tuple=()):
        """IOPair constructor.

        Parameters
        ----------
        input_tuple : tuple | any
            The input tuple that should be stored in the input-output pair. If the input is not provided as a tuple,
            the constructor will take care of the necessary conversion.
        output_tuple : tuple | any
            The output tuple that should be stored in the input-output pair. If the output is not provided as a tuple,
            the constructor will take care of the necessary conversion.
        """
        if not isinstance(input_tuple, tuple):
            input_tuple = (input_tuple,)
        if not isinstance(output_tuple, tuple):
            output_tuple = (output_tuple,)
        self.input_tuple = input_tuple
        self.output_tuple = output_tuple

    def __str__(self):
        """Convert-to-string instance method"""
        return f"IOPair(input={self.input_tuple}, output={self.output_tuple})"

