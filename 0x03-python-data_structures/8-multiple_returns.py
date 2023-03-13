#!/usr/bin/python3
def multiple_returns(sentence):
    s_tuple = ()
    if len(sentence) == 0:
        s_tuple = 0, None
    else:
        s_tuple = len(sentence), sentence[0]
        return s_tuple
