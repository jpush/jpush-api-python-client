# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except (ImportError):
    from distutils.core import setup

__version__ = '3.0.2'

setup(
    name='jpush',
    version=__version__,
    description='JPush\'s officially supported Python client library',
    keywords=('JPush', 'JPush API', 'Android Push', 'iOS Push'),
    license='MIT License',
    long_description=open("README.rst", "r").read(),

    url='https://github.com/jpush/jpush-api-python-client',
    author='jpush',
    author_email='support@jpush.cn',

    packages=['jpush', 'jpush.push', 'jpush.device'],
    platforms='any',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],

    install_requires=[
        'requests>=1.2',
    ],
)
