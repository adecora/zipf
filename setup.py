from setuptools import setup

with open('./README.rst', 'r') as reader:
    long_description = reader.read()

setup(
    name='pyzipf-cora',
    version='0.1.1',
    author='Alejandro de Cora',
    description="Zipf's Law",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    packages=['pyzipf'],
    install_requires=[
        'matplotlib',
        'pandas',
        'scipy',
        'pyyaml',
        'pytest'],
    entry_points={
        'console_scripts': [
            'countwords = pyzipf.countwords:main',
            'collate = pyzipf.collate:main',
            'plotcounts = pyzipf.plotcounts:main']})
