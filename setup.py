from setuptools import setup

setup(name='ispell_stemmer',
      version='0.1',
      description='Stem words using ispell definitions',
      url='https://github.com/Herover/ispell_stemmer',
      author='Herover',
      author_email='hi+git@leonora.app',
      license='MIT',
      packages=['ispell_stemmer'],
      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=['bin/ispell-export-stem'],
      zip_safe=False)
