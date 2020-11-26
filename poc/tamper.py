#!/usr/bin/env python

def tamper(payload,  **kwargs):
    print(', '.join(['{}={!r}'.format(k, v) for k, v in kwargs.items()]))
    return payload