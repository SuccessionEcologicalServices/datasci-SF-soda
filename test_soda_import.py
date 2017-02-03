#!/usr/bin/env python

__author__ = "Eric Allen Youngson"
__email__ = "eayoungs@gmail.com"
__copyright__ = "Copyright 2017"
__license__ = "GNU Affero (GPLv3)"

"""
    This module provides tests for functions requesting data from the Socrata API (SODA) https://dev.socrata.com/consumers/getting-started.html
"""

import soda_import as si
import pytest


def test_simple_request():
    """ """

    url = 'https://data.sfgov.org/resource/6jnk-ty34.json'
    oFileNm = '6jnk-ty34'
    assert si.simple_request(url, oFileNm)
