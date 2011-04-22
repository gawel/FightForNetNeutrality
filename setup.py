from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='FightForNetNeutrality',
      version=version,
      description="This package is a WSGI middleware which allow to block some IP Address. By default the french parlement is denied.",
      long_description=open('README.txt').read(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='net neutrality wsgi',
      author='Gael Pasgrimaud',
      author_email='gael@gawel.org',
      url='http://reflets.info/wp-neutalityfr-la-neutralite-du-net-expliquee-de-maniere-optimalisee-a-muriel/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
