# -*- coding: utf-8 -*-
import re
import ast
try:
    from setuptools import setup
except (ImportError):
    from distutils.core import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('jpush/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='jpush',
    version=version,
    description='JPush\'s officially supported Python client library',
    keywords=('JPush', 'JPush API', 'Android Push', 'iOS Push'),
    license='MIT License',
    long_description=open("README.rst", "r").read(),

    url='https://github.com/jpush/jpush-api-python-client',
    author='jpush',
    author_email='support@jpush.cn',

    packages=['jpush', 'jpush.push', 'jpush.device', 'jpush.report', 'jpush.schedule'],
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
