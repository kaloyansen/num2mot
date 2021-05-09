#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Kaloyan Krastev Krastev, kaloyansen@gmail.com
# # # # # # # # # # # # # # # # # # # # # # # # # # #
import sys
from num2mot import num2mot as n2m


if len(sys.argv) < 2:
	print('try again, at least one argument needed, a number, please')
	exit(0)

getstr = sys.argv[1]
print(n2m(getstr))

exit(0)
