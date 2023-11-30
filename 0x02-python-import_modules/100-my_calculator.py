#!/usr/bin/python3
import sys
from calculator_1 import add, mul, sub, div
arg_list = sys.argv
if len(arg_list) != 4 :
    print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
    exit(1)
a = sys.argv[1]
operator = sys.argv[2]
b = sys.argv[3]

if not a.isnumeric() or not b.isnumeric():
    print("Invalid aurguments")
    exit(1)
a = int(a)
b = int(b)
if operator == '+':
    add(a, b)
elif operator == '-':
    sub(a, b)
elif operator == '*':
    mul(a, b)
elif operator == '/':
    div(a, b)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
