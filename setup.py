from setuptools import setup, find_packages


setup(
    name='homework',
    version='1.0.0',
    install_requires=[
        'pytest',
        'requests'
    ],
    packages=find_packages()
)