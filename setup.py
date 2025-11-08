from setuptools import setup

setup(
    name='packages',
    version='0.1',
    description='A sample Python package',
    author='John Doe',
    author_email='codingdestro@gmail.com',
    packages=['internal', 'models', 'app'],
    install_requires=[
        'tortoise-orm',
        'aiogram',
    ],
)