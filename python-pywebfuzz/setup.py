#!/usr/bin/env python

import sys
try:
    from setuptools import setup, find_packages
except:
    print("You do not have setuptools installed. http://pypi.python.org/pypi/setuptools")
    sys.exit(1)

VERSION = "0.6.1"

long_description = """pywebfuzz is a Python module to assist in the
identification of vulnerabilities in web applications through brute force methods.
The module does this by providing common testing values along with generators and
other utilities that would be helpful when fuzzing web applications.

pywebfuzz has the fuzzdb project implemented in Python classes for ease of use.

fuzzdb is just a collection of values for testing. The point is to provide many of
the values of the fuzzdb project cleaned up and available through Python classes
and namespaces. This makes it easier to use these values in your own test cases.
Effort was made to match the names up similarly to the folders and values files
from the fuzzdb project. This effort can sometimes make for some ugly looking
namespaces. This balance was struck so that familiarity with the fuzzdb project
would cross over in to the Python code. The exceptions come in with the replacement
of hyphens with underscores.
"""

classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Web Environment",
    "Intended Audience :: Security Testers",
    "License :: OSI Approved :: GPLv3",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Security :: Testing"
]

package_dir = {"pywebfuzz": "pywebfuzz"}

setup(name="pywebfuzz",
      version=VERSION,
      author="Nathan Hamiel",
      author_email="nhamiel@gmail.com",
      url="http://code.google.com/p/pywebfuzz/",
      download_url="http://pywebfuzz.googlecode.com/files/pywebfuzz_{0}.tar.gz".format(VERSION),
      license="GPLv3",
      description="A Python module to assist in fuzzing web applications",
      long_description=long_description,
      package_dir=package_dir,
      packages=["pywebfuzz"],
      include_package_data=True,
      classifiers=classifiers)