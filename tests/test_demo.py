# -*- coding: utf-8 -*-
from demo import demo


def test_get_title():  
    result = demo.get_title('http://www.google.com/')
    expect = 'Google'
    assert result == expect