from main import *


class Tests:
    def test_foo(self):
        """
        Test the foo method with variety of args
        """
        actual = foo("Hello", "world!")
        expected = "Hello world!"
        assert (
            actual == expected
        ), f'expected foo("Hello", "world!") to return "{expected}"; instead, it returned "{actual}".'

        actual = foo("Hello", "")
        expected = "Hello "
        assert (
            actual == expected
        ), f'expected foo("Hello", "") to return "{expected}"; instead, it returned "{actual}".'

        actual = foo("world!", "Hello")
        expected = "world! Hello"
        assert (
            actual == expected
        ), f'expected foo("world!", "Hello") to return "{expected}"; instead, it returned "{actual}".'

    def test_bar(self):
        """
        Test the bar method returns the proper text
        """
        actual = type(bar())
        expected = str
        assert (
            actual == expected
        ), f"expected bar() to return a string; instead, it returned a {actual}."

        actual = bar()
        expected = "Hello world!"
        assert (
            actual == expected
        ), f'expected bar() to return "{expected}"; instead, it returned a "{actual}."'

    def test_baz(self, capsys):
        """
        Test the baz method prints the proper text
        """
        baz()
        captured = capsys.readouterr()  # capture print output
        actual = captured.out
        expected = "Hello world!\n"
        assert (
            actual == expected
        ), f'expected calling baz() to print "{expected}"; instead, it printed "{actual}".'

    def test_main(self, capsys):
        """
        Test the main method
        """
        main()
        captured = capsys.readouterr()  # capture print output
        actual = captured.out
        expected = "Hello world!\nHello world!\nHello world!\n"
        assert (
            actual == expected
        ), f'expected calling main() to print "{expected}"; instead, it printed "{actual}".'
