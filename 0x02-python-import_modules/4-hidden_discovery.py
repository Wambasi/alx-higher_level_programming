#!/usr/bin/python3
import dis
with open('hidden_4.py', 'rb') as file:
    bytecode = file.read()
dis.dis(bytecode)
