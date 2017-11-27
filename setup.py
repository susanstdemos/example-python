import os
from codecs import open

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'readme.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(
  name='example-python',
  version='0.0.1',
  description='An example Python project for testing SourceClear scans',
  long_description=long_description,
  url='https://github.com/srcclr/example-python',
  author='SourceClear',
  author_email='something@sourceclear.com',
  license='MIT'
)
