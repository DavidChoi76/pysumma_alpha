import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import shlex
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)

setup(name='pysumma',
      version = '0.1',
      description = 'This is pySUMMA',
      url = 'https://github.com/DavidChoi76/pysumma_alpha',
      author = 'YoungDon Choi',
      author_email = 'yc5ef@virginia.edu',
      license = 'MIT',
      packages=['pysumma'],
      setup_requires=['pytest-runner', 'xarray'],
      tests_require=['pytest'],
      cmdclass = {'test': PyTest})
      #...,)

#      zip_safe=False)
