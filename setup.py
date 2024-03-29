from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in max_pos/__init__.py
from max_pos import __version__ as version

setup(
	name="max_pos",
	version=version,
	description="Max added value features to ERPNext Retail Domain",
	author="ERPMax",
	author_email="eng.bakraldubai@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
