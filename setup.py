from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ogo_helper/__init__.py
from ogo_helper import __version__ as version

setup(
	name="ogo_helper",
	version=version,
	description="Ogo API Helper",
	author="Rifaz Marikkar",
	author_email="rifaz@marikkar.net",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
