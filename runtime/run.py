#!/usr/bin/env python3

import argparse
import re
import pathlib
import sys
import random
import tempfile
import subprocess
import os
from functions import *
from enum import Enum


class ParseState(Enum):
    NORMAL_TEXT = 1
    DELIMITER_START = 2
    EXPRESSION = 3
    DELIMITER_END = 4


def eval_expressions(line, loc=None):
    state = ParseState.NORMAL_TEXT
    result = ""
    expression = ""

    for c in line:
        if c == '%' or (state in (ParseState.DELIMITER_START, ParseState.EXPRESSION) and c == '`'):
            next_state = {
                ParseState.NORMAL_TEXT: ParseState.DELIMITER_START,
                ParseState.DELIMITER_START: ParseState.EXPRESSION,
                ParseState.EXPRESSION: ParseState.DELIMITER_END,
                ParseState.DELIMITER_END: ParseState.NORMAL_TEXT
            }
            state = next_state[state]
            if state == ParseState.NORMAL_TEXT:
                # If the expression starts and ends with $ then strip. These are used to stop
                # markdown formatters doing weird things.
                if len(expression) > 2 and expression[0] == '$' and expression[-1] == '$':
                    expression = expression[1:-1]

                # If it starts with alphas and whitespace and =, then assume it's an assignment
                # expression and exec it instead, but return the result of the assignment.
                match = re.match(r"([a-zA-Z09 ]+)=.+", expression)
                if match:
                    var_name = match.group(1).strip()
                    exec("from functions import *", None, loc)
                    exec(expression, None, loc)
                    evaluated = loc[var_name]
                else:
                    evaluated = eval(
                        "exec('from functions import *') or " + expression, None, loc)

                # commaize the value if it looks like an integer.
                isint = True
                for c in str(evaluated):
                    if not c in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                        isint = False
                        break

                if isint:
                    evaluated = commaize(evaluated)

                result += str(evaluated)
                expression = ""
        else:
            if state == ParseState.DELIMITER_START:
                result += "%" + c
                state = ParseState.NORMAL_TEXT
            elif state == ParseState.DELIMITER_END:
                expression += "%" + c
                state = ParseState.EXPRESSION
            elif state == ParseState.EXPRESSION:
                expression += c
            elif state == ParseState.NORMAL_TEXT:
                result += c

    if state == ParseState.DELIMITER_START:
        result += "%"

    return result


def eval_markdown(inlines):
    config = {}
    section_locals = {}
    section_locals["config"] = config
    question_directive_expressions = []

    random_questions = []
    result = []
    for line in inlines:
        directive = r"\[([a-z]+)\]: <> \(`?([^`]+)`?\)"
        directive_match = re.match(directive, line)
        if directive_match:
            directive_kind = directive_match.group(1)
            directive_expression = directive_match.group(2)

            # Rewrite config expressions from config.foo = bar to config["foo"] = bar
            config_expr = r"config\.([a-z]+) = (.+)"
            config_match = re.match(config_expr, directive_expression)
            if config_match:
                directive_expression = f'config["{config_match.group(1)}"] = {config_match.group(2)}'

            exec("from functions import *", None, section_locals)
            exec(directive_expression, None, section_locals)

            if directive_kind == 'question':
                question_directive_expressions.append(directive_expression)

        else:
            if line.startswith("#"):
                if random_questions:
                    random.shuffle(random_questions)
                    result.extend(random_questions)
                    result.append("")
                evaluated = eval_expressions(line, section_locals)
                config = {}
                section_locals = {}
                section_locals["config"] = config
                random_questions = []
                directive_kind = None
                directive_expression = None
                result.append(evaluated)
            elif len(line.strip()) == 0:
                result.append("")
            else:
                is_random = section_locals["config"].get("randomorder", False)

                for _ in range(section_locals["config"].get("count", 1)):
                    _exec_all(question_directive_expressions, section_locals)
                    evaluated = eval_expressions(line, section_locals)
                    if is_random:
                        random_questions.append("(@) " + evaluated)
                    else:
                        result.append("(@) " + evaluated)

                question_directive_expressions = []

    if random_questions:
        random.shuffle(random_questions)
        result.extend(random_questions)
        result.append("")

    return result


def _exec_all(expressions, local):
    exec("from functions import *", None, local)
    for expression in expressions:
        exec(expression, None, local)


def eval_markdown_file(infile, outfile):
    with open(infile, 'r') as f:
        lines = f.read().splitlines()

    outlines = eval_markdown(lines)

    with open(outfile, 'w') as out:
        for line in outlines:
            out.write(line + "\n")


# def invoke_pandoc(input_path, output_path):
#     subprocess.check_output(
#         ["pandoc",
#          "--from=markdown",
#          "--standalone",
#          "--mathjax",
#          "-t",
#          "html",
#          input_path,
#          output_path], universal_newlines=True)


def main():
    parser = argparse.ArgumentParser(
        description='Generates markdown question sets.')
    parser.add_argument('input', type=pathlib.Path)
    parser.add_argument('output', type=pathlib.Path)
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: File doesn't exist: {args.input}", file=sys.stderr)
        exit(1)

    tmp_output = tempfile.TemporaryFile()
    eval_markdown_file(args.input, args.output)


if __name__ == "__main__":
    main()
