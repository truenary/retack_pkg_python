from setuptools import setup, find_packages

setup(
    name='Retack SDK',
    version='0.0.1',
    description='A package for monitoring and error reporting.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Truenary',
    author_email='contact@truenary.com',
    url='https://github.com/truenary/retack_pkg_python',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', 
    install_requires=[
        'requests>2.0.0',
    ],
)
