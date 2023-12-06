#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
      name='medalgrouputils',
      version='0.1.0',
      description='Utilities for research in the Medal Group',
      author='The Medal Group',
      author_email='hmedal@utk.edu',
      url='https://github.com/medalgrouputk/util/',      
      install_requires=[ 
            "IPython",
            "matplotlib",
            "numpy",
            "numpy-stl", 
       	    "networkx",
            "pandas",
            "plotly",
      ],
      packages=find_packages(),
      package_data={'util': ['data/*']},
)
