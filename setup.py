from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = "MLOPS",
    version = "1.0.0",
    author = "Mohamed Hassan",
    packages = find_packages(),
    install_requires = requirements
)