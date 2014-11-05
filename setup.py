from distutils.core import setup

with open("README.rst") as rfile:
    long_description = rfile.read()

setup(
    name='python-libnessus',
    version='1.0.0.0',
    author='Ronald Bister and Mike Boutillier',
    author_email='mini.pelle@gmail.com/michael.boutillier@gmail.com',
    packages=['libnessus', 'libnessus.objects', 'libnessus.plugins'],
    install_requires=[
            'jsonpickle',
        ],
    url='http://pypi.python.org/pypi/python-libnessus/',
    license='Creative Common "Attribution" license (CC-BY) v3',
    description=('Python Nessus module to parse, chat with XMLRPC API, ...'),
    long_description=long_description,
    classifiers=["Development Status :: 4 - Beta",
                 "Environment :: Console",
                 "Programming Language :: Python :: 2.6",
                 "Programming Language :: Python :: 2.7",
                 "Topic :: System :: Networking"]
)
