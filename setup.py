from setuptools import setup

setup(name='ispell_stemmer',
      version='0.1',
      description='Stem words using ispell definitions',
      url='',
      author='Herover',
      author_email='leon.l.a.nielsen@gmail.com',
      license='MIT',
      packages=['ispell_stemmer'],
      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=['bin/ispell-export-stem'],
      zip_safe=False)