# -*- coding: utf-8
"""An example module.

.. moduleauthor:: chairco <chairco@gmail.com>

"""

from __future__ import print_function

import requests  
from lxml import html


def get_title(url):
    """Get the title of a web page.

    :param url: url of web page.
    :type url: str
    :returns: title of web page.
    :rtype: str

    >>> from demo import demo
    >>> demo.get_title('http://www.google.com/')
    'Google'

    .. versionadded:: 0.0.1

    """
    page = requests.get(url)
    root = html.fromstring(page.text)
    return root.findtext('.//title')


if __name__ == '__main__':  
    print(get_title('http://www.google.com/'))
