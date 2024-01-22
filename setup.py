from setuptools import setup, find_packages
import pkg_resources

install_requires = [
    'numpy',
    'networkx',
    'torchvision',
    'pandas',
]

setup(
    name='mss',
    version='0.0.1',
    author='Gezhi Xiu',
    packages=['mss'],
    install_requires=install_requires,
)
