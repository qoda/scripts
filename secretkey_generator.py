#!/usr/bin/env python
import random
from string import digits, punctuation, letters


return_string = ""
for i in xrange(50):
    choice_set = random.choice([digits, punctuation, letters])
    return_string += random.choice(choice_set)

print return_string
