import unittest

from run import *


class TestRun(unittest.TestCase):
    def test_no_expression(self):
        self.assertEqual(eval_expressions("hello"), "hello")
        self.assertEqual(eval_expressions("100%"), "100%")
        self.assertEqual(eval_expressions("%100%"), "%100%")
        self.assertEqual(eval_expressions("%10%0%"), "%10%0%")

    def test_simple_expression(self):
        self.assertEqual(eval_expressions("hello %%25%%"), "hello 25")
        self.assertEqual(eval_expressions("hello %%5 * 5%%"), "hello 25")

    def test_expression_alt_syntax(self):
        self.assertEqual(eval_expressions("hello %`5+5`%"), "hello 10")

    def test_function_calls(self):
        self.assertEqual(eval_expressions(
            "I %%repeat(2, 'like')%%"), "I likelike")

    def test_locals(self):
        locals = {}
        self.assertEqual(eval_expressions(
            "I %%a = 5%%", locals), "I 5")
        self.assertEqual(eval_expressions(
            "Now a is %%a%%", locals), "Now a is 5")
        self.assertEqual(eval_expressions(
            "Cool thing - %%repeat(4, a)%%", locals), "Cool thing - 5,555")

    def test_expression_with_percent(self):
        self.assertEqual(eval_expressions("%%5 % 10%%"), "5")

    def test_multiple_expressions(self):
        self.assertEqual(eval_expressions(
            "First: %%1 + 2%% and second: %%2 + 3%%"), "First: 3 and second: 5")

    def test_trailing_expresion(self):
        self.assertEqual(eval_expressions(
            "So: %%1+2"), "So: ")
        self.assertEqual(eval_expressions(
            "So: %%1+2%"), "So: ")

    def test_escaped_expression(self):
        self.assertEqual(eval_expressions("%%$a=10**5$%%", {}), "100,000")

    def test_eval_markdown(self):
        result = eval_markdown([
            "# My Quiz",
            "",
            r'Write $10%%repeat(5, r" \times 10")%%$ with an exponent.',
            '',
            'How many zeroes are in the standard form of $10^{%%4%%}$? Write this number in standard form.'
        ])

        self.assertListEqual(result, [
            "# My Quiz",
            "",
            r"(@) Write $10 \times 10 \times 10 \times 10 \times 10 \times 10$ with an exponent.",
            "",
            "(@) How many zeroes are in the standard form of $10^{4}$? Write this number in standard form."
        ])

    def test_eval_markdown_with_directives(self):
        result = eval_markdown([
            "# Title",
            "## Section",
            "",
            "[section]: <> (a = 5)",
            "This is a question with %%a%%"
        ])

        self.assertListEqual(result, [
            "# Title",
            "## Section",
            "",
            "(@) This is a question with 5"
        ])

    def test_eval_markdown_with_config(self):
        result = eval_markdown([
            "# Title",
            "## Section",
            "",
            "[section]: <> (config.randomorder = True)",
            "This is a question"
        ])

        self.assertListEqual(result, [
            "# Title",
            "## Section",
            "",
            "(@) This is a question",
            ""
        ])

    def test_eval_markdown_with_directives_escaped(self):
        result = eval_markdown([
            "# Title",
            "## Section",
            "",
            "[section]: <> (`answer=5`)",
            "This is a question with %`answer`%"
        ])

        self.assertListEqual(result, [
            "# Title",
            "## Section",
            "",
            "(@) This is a question with 5"
        ])


if __name__ == "__main__":
    unittest.main()
