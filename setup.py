from setuptools import setup, find_packages

with open("README.rst") as rfile:
    long_description = rfile.read()

setup(
    name='python-libnessus',
    version='1.0.0.1',
    author='Ronald Bister and Mike Boutillier',
    author_email='mini.pelle@gmail.com/michael.boutillier@gmail.com',
    packages=find_packages(exclude=["*.test"]),
    install_requires=[
            'jsonpickle',
        ],
    url='https://github.com/bmx0r/python-libnessus',
    download_url='https://github.com/bmx0r/python-libnessus/tarball/1.0.0.1',
    license='Creative Common "Attribution" license (CC-BY) v3',
    description=('Python Nessus module to parse, chat with XMLRPC API, ...'),
    long_description=long_description,
    classifiers=["Development Status :: 4 - Beta",
                 "Environment :: Console",
                 "Programming Language :: Python :: 2.6",
                 "Programming Language :: Python :: 2.7",
                 "Programming Language :: Python :: 3.3",
                 "Topic :: System :: Networking"]
)
