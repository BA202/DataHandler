#!/usr/bin/env python

from distutils.core import setup

version = "0.3.1"
setup(name='data_handler',
      version=version,
      description='Command line utilities for data analysis',
      author='Tobias Rothlin',
      author_email='tobias@rothlin.com',
      url='https://github.com/BA202/DataHandler',
      classifiers=[
            'Development Status :: 4 - Beta',
            'Programming Language :: Python',
            'Intended Audience :: System Administrators',
            'Topic :: Terminals',
            ],
      download_url="http://github.com/downloads/bitly/data_hacks/data_hacks-%s.tar.gz" % version,
      scripts = ['data_hacks/histogram.py', 
                'data_hacks/ninety_five_percent.py',
                'data_hacks/run_for.py',
                'data_hacks/bar_chart.py',
                'data_hacks/sample.py']
     )