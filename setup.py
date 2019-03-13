from os import path
from setuptools import setup


def readme():
    here = path.abspath(path.dirname(__file__))

    with open(path.join(here, 'README.rst'), encoding='UTF-8') as f:
        return f.read()

setup(
    name='notebooks',
    version='0.2.0',

    #long_description=readme(),

    url='https://github.com/SrMouraSilva/rbm_notebooks',

    author='Paulo Mateus Moura da Silva (SrMouraSilva)',
    author_email='mateus.moura@ppgcc.ifce.edu.br',
    maintainer='Paulo Mateus Moura da Silva (SrMouraSilva)',
    maintainer_email='mateus.moura@ppgcc.ifce.edu.br',

    license="Apache Software License v2",

    packages=[
        'machine_learning',
    ],
    package_data={},
    install_requires=[],

    test_suite='test',
    tests_require=['pytest', 'pytest-cov'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='rbm',

    platforms='Linux',
)
