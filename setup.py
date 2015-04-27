import sys
from setuptools import setup, find_packages

required_packages = [
	u'requests',
]

setup(
    name='pleercom-py',
    version='0.1.1',
    description='Pleer.com API Wrapper',
    author='Rustem Sayargaliev',
    author_email='r.sayargaliev@gmail.com',
    license='MIT',
    url='https://github.com/amureki/pleercom-py.git',
    packages=find_packages(),
    install_requires=required_packages,
    zip_safe=False
)