# SPDX-License-Identifier: MIT


# Import both local and third-party setup modules.
import codecs
import os

from setuptools import find_packages, setup

# Import local modules to fetch version number.
from avro import __description__, __version__

# Constants.
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as fh:
    long_description = '\n' + fh.read()


# Call the setup function.
setup(
    name='avro.py',
    version=__version__,
    description=__description__,
    long_description_content_type='text/markdown',
    long_description=long_description,
    author='HitBlast',
    author_email='hitblastlive@gmail.com',
    url='https://github.com/hitblast/avro.py',
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    package_data={'avro': ['*.md']},
    include_package_data=True,
    license='MIT',
    python_requires='>=3.8',
    keywords=[
        'python',
        'phonetics',
        'avro',
        'avro phonetic',
        'bangla',
        'bengali',
        'bengali phonetics',
        'transliteration',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    extras_require={
        'cli': ['click>=8.0.0', 'pyclip >= 0.7.0'],
    },
    entry_points={
        'console_scripts': [
            'avro=avro.cli:main',
        ],
    },
)
