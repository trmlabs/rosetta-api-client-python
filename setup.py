import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='rosetta-api-client-python',
    author='AUTHOR',
    author_email='AUTHOR_EMAIL',
    description='A python client for interacting with Rosetta endpoints',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blockjoe/rosetta-api-client-python",
    packages=setuptools.find_packages(),
    license='Apache License 2.0',
    python_requires='>=3.7',
    install_requires=[
        'pydantic',
        'requests'
    ]
)
