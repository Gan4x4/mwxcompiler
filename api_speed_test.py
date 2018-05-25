# -*- coding: utf-8 -*-

"""
Wrapper for compile standalone logo code

"""

__author__ = "Gan4x4 <gan4x4@gmail.com>"


import argparse
import json
import time

from LogoParser import Parser

data = {
    'error': 0,
    'message': '',
    'time': 0,
    'payload': False
}

try:
    p = argparse.ArgumentParser()
    p.add_argument('code', help="Logo code fo translate")
    cmd_args = p.parse_args()

    parser = Parser()
    start_time = int(round(time.time() * 1000))
    data['payload'] = parser.translate_from_anywhere(cmd_args.code)
    end_time = int(round(time.time() * 1000))
    data['time'] = end_time-start_time
except Exception as e:
    data['error'] = 1
    data['message'] = format(e)

json_data = json.dumps(data)
print(json_data)
