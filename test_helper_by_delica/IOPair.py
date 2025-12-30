class IOPair:
    """Class for easily defining input-output pairs."""
    def __init__(self, input_tuple=(), output_tuple=()):
        """IOPair constructor

        Parameters
        ----------
        input_tuple : tuple | any
            The input tuple that should be stored in the input-output pair. If the input is not provided as a tuple,
            the constructor will take care of the necessary conversion.
        output_tuple : tuple | any
            The input tuple that should be stored in the input-output pair. If the input is not provided as a tuple,
            the constructor will take care of the necessary conversion.
        """
        if not isinstance(input_tuple, tuple):
            input_tuple = (input_tuple,)
        if not isinstance(output_tuple, tuple):
            output_tuple = (output_tuple,)
        self.input_tuple = input_tuple
        self.output_tuple = output_tuple

    def __str__(self):
        return f"IOPair(input={self.input_tuple}, output={self.output_tuple})"