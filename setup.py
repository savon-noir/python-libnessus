from distutils.core import setup

with open("README.rst") as rfile:
    long_description = rfile.read()

setup(
    name='python-libnessus',
    version='0.0.1',
    author='Ronald Bister',
    author_email='mini.pelle@gmail.com',
    packages=['libnessus', 'libnessus.objects'],
    url='http://pypi.python.org/pypi/python-libnessus/',
    license='Creative Common "Attribution" license (CC-BY) v3',
    description=('Python Nessus module to parse, chat with XMLRPC API, ...'),
    long_description=long_description,
    classifiers=["Development Status :: 5 - Production/Stable",
                 "Environment :: Console",
                 "Programming Language :: Python :: 2.6",
                 "Programming Language :: Python :: 2.7",
                 "Topic :: System :: Networking"]
)
