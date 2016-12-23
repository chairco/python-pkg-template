# -*- coding: utf-8 -*-
"""
    Demo
    ~~~~

    Just a simplest project to show you how to build your own project.

    :copyright: (c) 2016 by chairco <chairco@gmail.com>.
    :license: BSD.
"""

import uuid

from pip.req import parse_requirements  
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import demo


def requirements(path):  
    return [str(r.req) for r in parse_requirements(path, session=uuid.uuid1())]


class Tox(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['-v', '-epy']
        self.test_suite = True

    def run_tests(self):
        import tox
        tox.cmdline(self.test_args)


setup(  
    name='demo',
    version=demo.__version__,
    author=demo.__author__,
    author_email=demo.__email__,
    url='http://your.host.name/demo',
    description='Just a simplest project to show you how to build your own project.',
    long_description=__doc__,
    packages=find_packages(),
    install_requires=requirements('requirements.txt'),
    tests_require=['tox'],
    cmdclass={'test': Tox},
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)