# -*- coding: utf-8 -*-

from setuptools import setup


from jpush import __version__

setup(
    name='jpush',
    version=__version__,
    description='JPush\'s officially supported Python client library',
    keywords=('JPush', 'JPush API'),
    license='MIT License',
    long_description=open("README.rst", "r").read(),

    url='https://github.com/jpush/jpush-api-python-client',
    author='linbo',
    author_email='llbgurs@gmail.com',

    packages=['jpush'],
    platforms='any',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
