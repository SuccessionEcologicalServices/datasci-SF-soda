#!/usr/bin/env python

__author__ = "Eric Allen Youngson"
__email__ = "eayoungs@gmail.com"
__copyright__ = "Copyright 2017"
__license__ = "GNU Affero (GPLv3)"

"""
    This module provides functions for requesting data from the Socrata API
    (SODA) https://dev.socrata.com/consumers/getting-started.html

    Starting point for this code base can be found @:
    https://dev.socrata.com/foundry/data.sfgov.org/75rg-imyz
"""

import requests
import json


def simple_request(url, oFileNm):
    """ """

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open(oFileNm+'.json', 'w') as the_file:
            json.dump(data, the_file)
        
        return True
