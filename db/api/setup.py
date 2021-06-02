# -*- coding: utf-8 -*-

""" Setup file for CouchClient.
"""
import sys

from setuptools import setup, find_packages
from pkg_resources import VersionConflict, require

import CouchClient as couch

try:
    require("setuptools>=38.3")
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)


if __name__ == "__main__":
    setup(
        name=couch.__title__,
        version=couch.__version__,
        packages=find_packages(exclude=["tests"]),
        install_requires=[
            "certifi==2020.4.5.1",
            "chardet==3.0.4",
            "idna==2.9",
            "pycouchdb==1.14",
            "requests==2.23.0",
            "urllib3==1.26.5",
        ],
        include_package_data=True,
        zip_safe=False,
        author=couch.__author__,
        author_email=couch.__author_email__,
        description=couch.__description__,
        license=couch.__license__,
        keywords=couch.__keywords__,
        url=couch.__url__,
        project_urls=couch.__project_urls__,
    )
