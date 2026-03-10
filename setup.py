from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = "AI_ANIME_RECOMMENDER",
    version = "0.1",
    author = "Mohamed Hassan",
    packages = find_packages(),
    install_requires = requirements
)