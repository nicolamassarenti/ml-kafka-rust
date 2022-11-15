import unittest


class TestInit(unittest.TestCase):
    def test_import(self):
        """
        Test that the data_generator package can be imported
        """
        # Arrange
        import data_generator

        # Act
        # Assert
        self.assertIsNotNone(data_generator)

    def test_version(self):
        """
        Test that the data_generator package has a version
        """
        # Arrange
        import data_generator

        # Act
        # Assert
        self.assertIsNotNone(data_generator.__version__)

    def test_logger(self):
        """
        Test that the data_generator package has a logger
        """
        # Arrange
        import data_generator

        # Act
        # Assert
        self.assertIsNotNone(data_generator.logger)

    def test_exception_raise(self):
        """
        Test that the data_generator decoretor function `wrapper` logs an exception when an exception is raised
        """
        # Arrange
        import data_generator

        # Act
        # Assert
        with self.assertRaises(ValueError):

            @data_generator.log
            def test():
                raise ValueError("test")

            test()

    def test_log(self):
        """
        Test that the data_generator decoretor function `wrapper` logs the function name and arguments
        """
        # Arrange
        import data_generator

        # Act
        # Assert
        @data_generator.log
        def test(a: str, b: str):
            pass

        test("hello", "world")
