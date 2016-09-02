from distutils.core import setup

setup(
	name='PyMets',
	version='0.1.0',
	author='Sean Mosely',
	author_email='sean.mosely@gmail.com',
	packages=['pymets','pymets.tests'],
	description='Python library for building METS XML documents',
	install_requires=['lxml'])