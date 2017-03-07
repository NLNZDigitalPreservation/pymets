try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION="0.1.2"

config = {
	'name':'pymets',
	'version': VERSION,
	'author':'Sean Mosely',
	'author_email':'sean.mosely@gmail.com',
	'packages':['pymets'],
	'description':'Python library for building METS XML documents',
	'install_requires':['lxml==3.6.4',],
	'download_url': 'https://github.com/NLNZDigitalPreservation/pymets/archive/v'+VERSION+'.tar.gz',
	'license': 'MIT',
	}

setup(**config)