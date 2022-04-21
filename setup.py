import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='test',
    version='0.0.1',
    author='VP',
    author_email='vishnu.priya@innoboon.com',
    description='Testing installation of Package',
    long_description=long_description,
    url='https://github.com/VishnuPriyaIB/test',
    license='MIT',
    packages=['test'],
)