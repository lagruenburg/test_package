from setuptools import setup

from my_pip_package import _version_

setup(
	name = 'my_pip_package',
	version = _version_,
	
	url = 'https://github.com/lagruenburg/test_package',
	author = 'Laura Gruenburg',
	author_email = 'lagruenburg@gmail.com',

	py_modules = ['my_pip_package'],
)