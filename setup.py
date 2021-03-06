"""Cloud Mesh: managing multiple virtual machines in Clouds

This project allows you to manage multiple virtual machines.
In future you will be able ta add multipl eclouds.
"""

from setuptools import setup, find_packages
import sys, os


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()

def desc():
    info = read('README.md')
    try:
        return info + '\n\n' + read('CHANGES.txt')
    except IOError:
        return info

version = read("VERSION.txt")


classifiers = """\
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: Science/Research
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: Apache Software License
Programming Language :: Python
Topic :: Database
Topic :: Software Development :: Libraries :: Python Modules
Operating System :: POSIX :: Linux
Programming Language :: Python :: 2.7
Operating System :: MacOS :: MacOS X
Topic :: Scientific/Engineering
Topic :: System :: Clustering
Topic :: System :: Distributed Computing
"""

if sys.version_info < (2, 7):
    _setup = setup
    def setup(**kwargs):
        if kwargs.has_key("classifiers"):
            del kwargs["classifiers"]
        _setup(**kwargs)

doclines = __doc__.split("\n")

setup(
    name='flask_cm',
    version=version,
    description = doclines[0],
    classifiers = filter(None, classifiers.split("\n")),
    long_description = desc(),
    keywords='Cloud FutureGrid Flask farmework',
    maintainer='Gregor von Laszewski',
    maintainer_email="laszewski@gmail.com",
    author='Gregor von Laszewski',
    author_email='laszewski@gmail.com',
    url='https://github.com/futuregrid/flask_cm',
    license='Apache 2.0',
    package_dir = {'': '.'},
    packages = find_packages(exclude=['ez_setup', 'examples', 'tests']),
    
    #include_package_data=True,
    zip_safe=False,
    
#    entry_points={
#        'console_scripts': [
#                'cm = fgvirtualcluster.FGCluster:commandline_parser',
#                'fg-csh = fgvirtualcluster.FGShell:main',
#             ]},

    install_requires = [
        'setuptools',
        'pip',
        'docopt',
        'pyyaml',
        'Flask>=0.7',
        'Flask-WTF>=0.6'
        'paramiko',
        'blessings',
        'fabric',
        'progress',
        'sh',
        "console",
        ],

#    scripts=['bin/cm', 'bin/cm']

    )

# pycrypto
