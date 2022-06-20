from importlib.metadata import entry_points
import sys

from setuptools import setup, find_packages

import ssg

setup(
    name='ssg',
    version=ssg.__version__,
    author=ssg.__author__,
    license=ssg.__licence__,
    author_email='ilya.blan4@gmail.com',
    description=ssg.__doc__.strip(),
    python_requires='>=3.10',
    packages=find_packages(include=['ssg', 'ssg.*']),
    entry_points={
        'console_scripts': [
            'ssg = ssg.__main__:main',
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Environment :: Console',
        'Topic :: Utilities'
    ]
)
