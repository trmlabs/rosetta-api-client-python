import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='rosetta-api-client-python',
    author='blockjoe, gretha',
    author_email='joehabel46@gmail.com',
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
    ],
    extras_require = {
        'dev' : ['datamodel-code-generator', 'sphinx', 'sphinx-rtd-theme', 'm2r2']
    }
)
