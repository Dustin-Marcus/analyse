from setuptools import setup, find_packages

setup(
    name='analyse',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Dustin-Marcus/analyse.git',
    author='Dustin Marcus',
    author_email='dustin.marcus01@gmail.com'
)