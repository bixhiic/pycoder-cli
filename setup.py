from setuptools import setup

setup(
    name='pycoderCli',
    version='0.1.0',
    py_modules=['pycodercli'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'pycodercli = pycodercli:cli',
        ],
    },
)