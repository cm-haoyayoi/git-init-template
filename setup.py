#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages


def main():
    setup(
        name='Test',
        version='0.0.1',
        description='Test',
        author='your name',
        author_email='your_name@example.jp',
        packages=find_packages(),
        test_suite='nose.collector',
        zip_safe=False,
        include_package_data=True
    )


if __name__ == '__main__':
    main()
