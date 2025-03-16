from setuptools import setup, find_packages

setup(
    name='colablib',
    version='0.1.8',
    packages=find_packages(),
    install_requires=[
        'safetensors',
        'requests',
        'tqdm',
        'PyYAML',
        'gdown',
        'toml',
        'rarfile',
        'xmltodict',
        'pydantic'
    ],
    author='Ericyoung',
    author_email='',
    description='A utility library for Google Colab',
    url='https://github.com/gishare/colablib',
)
