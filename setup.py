from setuptools import setup, find_packages



# Read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='PyBuild',
    version='0.1.0',
    author='A-Boring-Square',
    author_email='aboringsquare@gmail.com',
    description='A Python library to programmatically build your Python programs.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/A-Boring-Square/PyBuild',  # Replace with your actual URL
    packages=find_packages(),
    include_package_data=True,
    py_modules=['Build'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'pyinstaller',  # Add pyinstaller as a dependency
    ],
)
