from setuptools import setup

setup(name='pysumma',
      version = '0.1',
      description = 'This is pySUMMA',
      url = '',
      author = 'Choi',
      author_email = 'yc5ef@virginia.edu',
      license = 'MIT',
      packages=['pysumma'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)