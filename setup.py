try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION="v0.1.0~git"

config = {
	'name':'pymets',
	'version':'0.1.0',
	'author':'Sean Mosely',
	'author_email':'sean.mosely@gmail.com',
	'packages':['pymets'],
	'description':'Python library for building METS XML documents',
	'install_requires':['lxml==3.6.4',],
	'download_url': 'https://github.com/NLNZDigitalPreservation/pymets/archive/'+VERSION+'.tar.gz',}

setup(**config)