#!/usr/bin/env python
from setuptools import setup


# PyPi requires reStructuredText instead of Markdown,
# so we convert our Markdown README for the long description
try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   long_description = open('README.md').read()

# Command-line tools
entry_points = {'console_scripts': [
    'rpub = rpub:rpub',
    'rpub-update = rpub:rpub_update',
    'rpub-add = rpub:rpub_add',
    'rpub-delete = rpub:rpub_delete',
    'rpub-import = rpub:rpub_import',
    'rpub-export = rpub:rpub_export',
    'tpub-plot = tpub:tpub_plot',
    'tpub-spreadsheet = tpub:tpub_spreadsheet'
]}

setup(name='rpub',
      version='1.1.0',
      description="A simple tool to keep track of the publications related "
                  "to NASA's TESS mission.",
      long_description=long_description,
      author='Rob Zellem',
      author_email='robert.t.zellem@nasa.gov',
      license='MIT',
      url='',
      packages=['rpub'],
      data_files=[('rpub/templates', ['rpub/templates/template.md', 'rpub/templates/template-overview.md'])],
      install_requires=["jinja2",
                        "six",
                        "astropy",
                        "ads",
                        "tqdm"],
      entry_points=entry_points,
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Intended Audience :: Science/Research",
          "Topic :: Scientific/Engineering :: Astronomy",
          ],
      )
