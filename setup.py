import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version='0.0.3'

setuptools.setup(
    name='data_handler',
    version='0.0.3',
    author='Tobias Rothlin',
    author_email='tobias@rothlin.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/BA202/DataHandler',
    license='MIT',
    packages=['toolbox'],
    install_requires=['requests'],
)