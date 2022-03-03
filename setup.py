from setuptools import setup, find_packages

from my_pip_package import __version__

setup(
    name='data_handler_package',
    version=__version__,

    url='https://github.com/BA202/DataHandler',
    author='Tobias Rothlin',
    author_email='tobias@rothlin.com',

    py_modules=['DataHandler'],
    license='MIT',
    packages=find_packages(),
    description="A interface to load data from a local server",
        classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)